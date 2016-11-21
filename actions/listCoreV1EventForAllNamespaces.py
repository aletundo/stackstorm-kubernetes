from lib import k8s

from st2actions.runners.pythonrunner import Action

class listCoreV1EventForAllNamespaces(Action):

    def run(self,fieldSelector=None,labelSelector=None,pretty=None,resourceVersion=None,timeoutSeconds=None,watch=None):

        myk8s = k8s.K8sClient(self.config)

        args = {}
        if fieldSelector is not None:
          args['fieldSelector'] = fieldSelector
        if labelSelector is not None:
          args['labelSelector'] = labelSelector
        if pretty is not None:
          args['pretty'] = pretty
        if resourceVersion is not None:
          args['resourceVersion'] = resourceVersion
        if timeoutSeconds is not None:
          args['timeoutSeconds'] = timeoutSeconds
        if watch is not None:
          args['watch'] = watch

        return myk8s.runAction('listCoreV1EventForAllNamespaces', **args)