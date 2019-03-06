from tethys_sdk.base import TethysAppBase, url_map_maker


class ChrisDesign(TethysAppBase):
    """
    Tethys app class for Chris Design.
    """

    name = 'Chris Design'
    index = 'chris_design:proposal'
    icon = 'chris_design/images/snoicon1.png'
    package = 'chris_design'
    root_url = 'chris-design'
    color = '#209970'
    description = 'CEEN 514 Assignment: Design'
    tags = '&quot;Practice&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='proposal',
                url='chris-design',
                controller='chris_design.controllers.proposal'
            ),
            UrlMap(
                name='wireframe',
                url='chris-design/wireframe',
                controller='chris_design.controllers.wireframe'
            ),
        )

        return url_maps
