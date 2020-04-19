Blacklists for Italian Network Operators

Italian Network Operators MUST implement at least five different
blacklists (DNS sinkhole) in order to comply with Italian laws.

It means that customers using their Italian ISP's resolvers must not reach those
forbidden resources.

There are four main species of lists:

- CNCPO (pedo-porn sites)
- AAMS (illegal gambling sites and illegal tobacco sites)
- AGCOM (copyright infringement cases)
- MANUAL (lists provided by Italian LEAs or other Authorities)

Here is a bundle of scripts able to get the lists, parse the data and produce a
DNS file (currently for Unbound) to hijack some queries toward a customized stop
page.