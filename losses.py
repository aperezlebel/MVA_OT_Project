"""Implement the loss functions for the NN example."""
import numpy as np
from abc import ABC, abstractmethod

import activations as act


class BaseLoss(ABC):
    """Abstract class for loss classes."""

    def __call__(self, y1, y2):
        """Shortcut to call the loss function."""
        return self.loss(y1, y2)

    @staticmethod
    @abstractmethod
    def loss(y1, y2):
        """Implement the loss function."""
        return

    @staticmethod
    @abstractmethod
    def derivative(y1, y2):
        """Implement the derivative of the loss function."""
        return


class Squared(BaseLoss):
    """Implement the squared loss function."""

    @staticmethod
    def loss(y1, y2):
        """Implement the squared loss.

        Args:
        -----
            y1 : np.array of shape (n,)
            y2 : np.array of shape (n,)

        Returns:
        --------
            l : np.array of shape (n,)

        """
        return np.power(y1 - y2, 2)/2

    @staticmethod
    def derivative(y1, y2):
        """Implement the first derivative of the squared loss.

        Args:
        -----
            y1 : np.array of shape (n,)
            y2 : np.array of shape (n,)

        Returns:
        --------
            l : np.array of shape (n,)

        """
        return y1 - y2


class Logistic(BaseLoss):
    """Implement the logistic loss function."""

    @staticmethod
    def loss(y1, y2):
        """Implement the logistic loss.

        Args:
        -----
            y1 : np.array of shape (n,)
            y2 : np.array of shape (n,)

        Returns:
        --------
            l : np.array of shape (n,)

        """
        sigmoid = act.Sigmoid.activation
        return -np.log(sigmoid(y1*y2))/np.log(2)

    @staticmethod
    def derivative(y1, y2):
        """Implement the first derivative of the logistic loss.

        Args:
        -----
            y1 : np.array of shape (n,)
            y2 : np.array of shape (n,)

        Returns:
        --------
            l : np.array of shape (n,)

        """
        sigmoid_d = act.Sigmoid.derivative
        return np.divide(y2, sigmoid_d(y1*y2))/np.log(2)
