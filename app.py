from epp.EPP import EPP, Contact, Domain, Nameserver

config = {
    'host': 'testdrs.domain-REGISTRY.nl', 
    'port': 700,
    'user': 'q',
    'pass': 'q',
    }

epp = EPP(**config)
