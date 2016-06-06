from .MyComponent import MyComponent


class DeviceLinkProvider(object):
    """Provide link from a device to its associated MyComponent."""

    def __init__(self, device):
        """Initialize this provider.

        device will be the device that may be associated with a MyComponent
        instance.

        """
        self.device = device

    def getExpandedLinks(self):
        """Return list of HTML snippets to add to device's links."""

        # Search for MyComponent instances with any of the MAC addresses
        # associated with our device. This requires that index_type and
        # index_scope be set on the MyComponent.macaddress property in
        # zenpack.yaml.
        results = MyComponent.class_search(
            self.getDmd(),
            None,
            macaddress=self.device.getMacAddresses())

        for result in results:
            try:
                # getObject() returns the object (MyComponent) to which a
                # catalog result points.
                return result.getObject()
            except Exception:
                # Sometimes catalog results are stale. That's OK.
                pass
