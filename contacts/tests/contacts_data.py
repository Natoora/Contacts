from contacts.tests.factories import (
    ContactPositionFactory,
    EmailRecipientListFactory,
)


def populate():
    """Contacts create contact position entries"""
    ContactPositionFactory.create(name="Operations Manager", sync_to_crm=True)
    ContactPositionFactory.create(name="Procurement/Goods In", sync_to_crm=True)
    ContactPositionFactory.create(name="Baker", sync_to_crm=True)
    ContactPositionFactory.create(name="Consultant", sync_to_crm=True)
    ContactPositionFactory.create(name="Production", sync_to_crm=True)
    ContactPositionFactory.create(name="Kitchen Manager", sync_to_crm=True)
    ContactPositionFactory.create(name="Kitchen", sync_to_crm=True)
    ContactPositionFactory.create(name="Chef/Owner", sync_to_crm=True)
    ContactPositionFactory.create(name="Store Manager", sync_to_crm=True)
    ContactPositionFactory.create(name="Sous Chef", sync_to_crm=True)
    ContactPositionFactory.create(name="Pastry Chef", sync_to_crm=True)
    ContactPositionFactory.create(name="General Manager", sync_to_crm=True)
    ContactPositionFactory.create(name="Restaurant Manager", sync_to_crm=True)
    ContactPositionFactory.create(name="Head Chef", sync_to_crm=True)
    ContactPositionFactory.create(name="Head Pastry Chef", sync_to_crm=True)
    ContactPositionFactory.create(name="Executive Chef", sync_to_crm=True)
    ContactPositionFactory.create(name="Chef De Partie", sync_to_crm=True)
    ContactPositionFactory.create(name="Bar Manager", sync_to_crm=True)
    ContactPositionFactory.create(name="Finance Departament", sync_to_crm=False)

    """ Contacts create email recipient list entries """
    EmailRecipientListFactory.create(
        name="Special price expiry",
        description="Recipients of the special prices expiring email",
        recipients="technology@natoora.com",
    )
    EmailRecipientListFactory.create(
        name="Exchange rate expiry",
        description="-",
        recipients="technology@natoora.com",
    )
