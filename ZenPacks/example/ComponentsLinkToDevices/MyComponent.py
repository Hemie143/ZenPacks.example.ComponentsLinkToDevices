# The schema module is created by zenpacklib and contains classes created by
# zenpacklib based on what's defined in zenpack.yaml.
from . import schema


class MyComponent(schema.MyComponent):
    """Overrides for the MyComponent class defined in zenpack.yaml."""

    def linked_device(self):
        """Return device linked to this component.

        Linkage is done via MAC address in this case.

        """
        # layer2_catalog provides fast lookup of NICs (IpInterface) by MAC
        # address.
        layer2_catalog = self.getDmdRoot('ZenLinkManager')._getCatalog(layer=2)

        # Return the first device associated with a NIC with our MAC address.
        for result in layer2_catalog(macaddress=self.macaddress):
            try:
                # result.getObject() returns the object to which a catalog
                # points. In this case that will be an IpInterface.
                return result.getObject().device()
            except Exception:
                # The catalog may contain stale references. That's OK.
                pass
