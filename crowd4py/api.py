# -*- coding: utf-8 -*-


class API:
    """crowd4u API"""
    def __init__(self, user_info='', project_name='', relation_name=''):
        """API instance Constructor
        :param user_info:
        :param project_name:
        :param relation_name:
        """

        self.user_info = user_info
        self.project_name = project_name
        self.relation_name = relation_name
        pass

    @property
    def relation_data(self):
        pass

    @property
    def task_assignment(self):
        pass


    pass
