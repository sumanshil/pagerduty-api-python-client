from .entity import Entity


class Rulesets(Entity):
    """PagerDuty user entity."""

    @classmethod
    def create(cls, data=None, api_key=None, **kwargs):
        return getattr(Entity, 'create').__func__(
            cls,
            data=data,
            api_key=api_key
        )

    def contact_methods(self, **kwargs):
        """Get all contact methods for this user."""
        endpoint = '/{0}/{1}/rules'.format(
            self.endpoint,
            self['id'],
        )
        result = self.request('POST', endpoint=endpoint, data=data,
                              query_params=kwargs)
        self._data['rulesets'].append(result['ruleset'])
        return result

    def delete_ruleset(self, id, **kwargs):
        """Delete a contact method for this user."""
        endpoint = '{0}/{1}'.format(
            self.endpoint,
            self['id']
        )
        return self.request('DELETE', endpoint=endpoint, query_params=kwargs)

    def delete_rule(self, id, **kwargs):
        """Delete a contact method for this user."""
        endpoint = '{0}/{1}/rules/{2}'.format(
            self.endpoint,
            self['id'],
            id
        )
        return self.request('DELETE', endpoint=endpoint, query_params=kwargs)

    def get_ruleset(self, id, **kwargs):
        """Delete a contact method for this user."""
        endpoint = '{0}/{1}'.format(
            self.endpoint,
            id
        )
        result = self.request('GET', endpoint=endpoint, query_params=kwargs)
        return result["ruleset"]

    def get_rule(self, id, **kwargs):
        """Delete a contact method for this user."""
        endpoint = '{0}/{1}/rules/{2}'.format(
            self.endpoint,
            self['id'],
            id
        )
        result = self.request('GET', endpoint=endpoint, query_params=kwargs)
        return result["rule"]

    def get_rulesets(self, **kwargs):
        """Delete a contact method for this user."""
        endpoint = '{0}'.format(
            self.endpoint
        )
        result = self.request('GET', endpoint=endpoint, query_params=kwargs)
        return result["rulesets"]

    def get_rules(self, **kwargs):
        """Delete a contact method for this user."""
        endpoint = '{0}/{1}/rules'.format(
            self.endpoint,
            self['id']
        )
        result = self.request('GET', endpoint=endpoint, query_params=kwargs)
        return result["rule"]

    def update_rulesets(self, *args, **kwargs):
        """Please implement me."""
        raise NotImplemented

    def update_rule(self, *args, **kwargs):
        """Please implement me."""
        raise NotImplemented
