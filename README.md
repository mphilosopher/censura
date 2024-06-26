# Blacklists for Italian Network Operators

Italian Network Operators MUST implement at least six different
blacklists (DNS sinkhole) in order to comply with the Italian laws.
It means that customers using their Italian ISP's resolvers must not reach those
forbidden resources.
There are five main species of lists:

- CNCPO [^0] (pedo-porn sites)
- AAMS (illegal gambling sites and illegal tobacco sites)
- AGCOM [^1] (copyright infringement cases)
- CONSOB (unlicensed financial services)
- IVASS [^2] (illegal insurance sites)
- MANUAL (lists provided by Italian LEAs or other Authorities)

Here is a bundle of scripts able to get the lists, parse the data and produce a
DNS file (currently for Bind, Unbound, and PowerDNS) to hijack some queries toward a customized stop
page.

[^0]: CNCPO has changed the way it distributes the list: it now only works through PEC.
To get software that also automates operations with CNCPO, take a look at this repository:
[kit-censura](https://github.com/robynhub/kit-censura)
[^1]: Piracy Shield is still managed by AGCOM, but it has its own platform, which we manage here through the [Compliance Guard software](https://github.com/OpenAccess-Italia/ComplianceGuard) 
[^2]: IVASS list has not been implemented by this software yet

~~CNCPO requires a procedure to register and get a client certificate in order to~~
~~retrieve the list. They provide a .pfx certificate (PKCS#12) with a password.~~
~~If you need to convert to PEM try the following commands (thanks to Daniele Carlini [@karlainz](https://github.com/karlainz)~~
~~for the feedback):~~\
~~`openssl enc -base64 -d -in cncpo.pfx -out cncpo-base64.pfx`~~
~~`openssl pkcs12 -in cncpo-base64.pfx -out cncpo.pem  -clcerts -nodes`~~
  
  
# Disclaimer

This software is provided ​“AS IS”. Developers make no other warranties, express or implied.

### Credits

The original tool [kit-censura](https://github.com/rfc1036/kit-censura) was written by Marco d'Itri <md@Linux.IT> [@rfc1036](https://github.com/rfc1036)  
Look also at this fork by [@robynhub](https://github.com/robynhub): [kit-censura](https://github.com/robynhub/kit-censura)
