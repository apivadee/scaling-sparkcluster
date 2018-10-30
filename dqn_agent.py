from collections import deque
import os
import numpy as np
import tensorflow as tf


class DQNAgent:

    def __init__(self, enable_actions, environment_name):
        self.name = os.path.splitext(os.path.basename(__file__))[0]
        self.enable_actions = enable_actions
        self.n_actions = len(self.enable_actions)
        self.minibatch_size = 32
        self.replay_memory_size = 1000
        self.learning_rate = 0.001
        self.discount_factor = 0.9
        self.exploration = 0.1
        self.model_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "kitwai_models")
        self.model_name = "spark"
        self.D = deque(maxlen=self.replay_memory_size)
        self.init_model()
        self.current_loss = 0.0

    def init_model(self):
        self.x = tf.placeholder(tf.float32, [None, 1, 8])
        x_flat = tf.reshape(self.x, [-1, 8])
        W_fc1 = tf.Variable(tf.truncated_normal([8, 8], stddev=0.01))
        b_fc1 = tf.Variable(tf.zeros([8]))
        h_fc1 = tf.nn.relu(tf.matmul(x_flat, W_fc1) + b_fc1)
        W_out = tf.Variable(tf.truncated_normal([8, self.n_actions], stddev=0.01))
        b_out = tf.Variable(tf.zeros([self.n_actions]))
        self.y = tf.matmul(h_fc1, W_out) + b_out
        self.y_ = tf.placeholder(tf.float32, [None, self.n_actions])
        self.loss = tf.reduce_mean(tf.square(self.y_ - self.y))
        optimizer = tf.train.RMSPropOptimizer(self.learning_rate)
        self.training = optimizer.minimize(self.loss)
        self.saver = tf.train.Saver()
        self.sess = tf.Session()
        self.sess.run(tf.global_variables_initializer())

    def Q_values(self, state):
        res = self.sess.run(self.y, feed_dict={self.x: [state]})[0]
        return res

    def select_action(self, state, epsilon):
        if np.random.rand() <= epsilon:
            return np.random.choice(self.enable_actions)
        else:
            return self.enable_actions[np.argmax(self.Q_values(state))]

    def store_experience(self, state, action, reward, state_1, terminal):
        self.D.append((state, action, reward, state_1, terminal))

    def experience_replay(self):
        state_minibatch = []
        y_minibatch = []
        minibatch_size = min(len(self.D), self.minibatch_size)
        minibatch_indexes = np.random.randint(0, len(self.D), minibatch_size)
        for j in minibatch_indexes:
            state_j, action_j, reward_j, state_j_1, terminal = self.D[j]
            action_j_index = self.enable_actions.index(action_j)
            y_j = self.Q_values(state_j)
            if terminal:
                y_j[action_j_index] = reward_j
            else:
                y_j[action_j_index] = reward_j + self.discount_factor * np.max(self.Q_values(state_j_1))  
            state_minibatch.append(state_j)
            y_minibatch.append(y_j)
        self.sess.run(self.training, feed_dict={self.x: state_minibatch, self.y_: y_minibatch})
        self.current_loss = self.sess.run(self.loss, feed_dict={self.x: state_minibatch, self.y_: y_minibatch})

    def load_model(self, model_path=None):
        if model_path:
            self.saver.restore(self.sess, model_path)
        else:
            checkpoint = tf.train.get_checkpoint_state(self.model_dir)
            if checkpoint and checkpoint.model_checkpoint_path:
                self.saver.restore(self.sess, checkpoint.model_checkpoint_path)

    def save_model(self):
        self.saver.save(self.sess, os.path.join(self.model_dir, self.model_name))
