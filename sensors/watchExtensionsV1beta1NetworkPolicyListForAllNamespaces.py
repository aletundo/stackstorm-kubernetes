from os import sys, path
if __name__ == '__main__' and __package__ is None:
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from sensor_base import SensorBase


class watchExtensionsV1beta1NetworkPolicyListForAllNamespaces(SensorBase):

    def __init__(
            self,
            sensor_service,
            config=None,
            extension="/apis/extensions/v1beta1/watch/networkpolicies",
            trigger_ref="kubernetes.networkpolicies"):
        super(  # pylint: disable=bad-super-call
            self.__class__,  # pylint: disable=bad-super-call
            self).__init__(
            sensor_service=sensor_service,
            config=config,
            extension=extension,
            trigger_ref=trigger_ref)
