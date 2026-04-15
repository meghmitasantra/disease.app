import numpy as np
from collections import Counter

class DecisionTreeNode:
    def __init__(self, depth=0, max_depth=None):
        self.depth = depth
        self.max_depth = max_depth
        self.feature_index = None
        self.threshold = None
        self.left = None
        self.right = None
        self.label = None

def gini(y):
    m = len(y)
    if m == 0:
        return 0
    counts = np.bincount(y)
    return 1 - sum((c/m)**2 for c in counts if c > 0)

def best_split(X, y, features):
    m = len(y)
    best_gain, best_idx, best_thresh = 0, None, None
    parent = gini(y)

    for idx in features:
        for thresh in np.unique(X[:, idx]):
            left = X[:, idx] <= thresh
            y_l, y_r = y[left], y[~left]

            if len(y_l) == 0 or len(y_r) == 0:
                continue

            gain = parent - (len(y_l)/m)*gini(y_l) - (len(y_r)/m)*gini(y_r)

            if gain > best_gain:
                best_gain, best_idx, best_thresh = gain, idx, thresh

    return best_idx, best_thresh

def majority_label(y):
    return Counter(y).most_common(1)[0][0]

def build_tree(X, y, depth=0, max_depth=None, max_features=None):
    node = DecisionTreeNode(depth, max_depth)

    if len(set(y)) == 1 or (max_depth and depth >= max_depth):
        node.label = majority_label(y)
        return node

    n = X.shape[1]
    features = range(n) if max_features is None else np.random.choice(n, max_features, False)

    idx, thresh = best_split(X, y, features)

    if idx is None:
        node.label = majority_label(y)
        return node

    node.feature_index = idx
    node.threshold = thresh

    left = X[:, idx] <= thresh
    node.left = build_tree(X[left], y[left], depth+1, max_depth, max_features)
    node.right = build_tree(X[~left], y[~left], depth+1, max_depth, max_features)

    return node

def predict_tree(node, x):
    if node.label is not None:
        return node.label
    return predict_tree(node.left if x[node.feature_index] <= node.threshold else node.right, x)

class RandomForestScratch:
    def __init__(self, n_estimators=10, max_depth=None, max_features=None):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.max_features = max_features
        self.trees = []

    def predict(self, X):
        preds = np.array([[predict_tree(t, x) for t in self.trees] for x in X])
        return np.array([Counter(row).most_common(1)[0][0] for row in preds])