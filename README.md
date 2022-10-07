Blacklists for Italian Network Operators

Italian Network Operators MUST implement at least five different
blacklists (DNS sinkhole) in order to comply with Italian laws.

It means that customers using their Italian ISP's resolvers must not reach those
forbidden resources.

There are four main species of lists:

- CNCPO[0] (pedo-porn sites)
- AAMS (illegal gambling sites and illegal tobacco sites)
- AGCOM (copyright infringement cases)
- MANUAL (lists provided by Italian LEAs or other Authorities)

Here is a bundle of scripts able to get the lists, parse the data and produce a
DNS file (currently for Bind and Unbound) to hijack some queries toward a customized stop
page.

[0] CNCPO requires a procedure to register and get a client certificate in order to
retrieve the list. They provide a .pfx certificate (PKCS#12) with a password.
If you need to convert to PEM try the following commands (thanks to Daniele Carlini
for the feedback):

openssl enc -base64 -d -in cncpo.pfx -out cncpo-base64.pfx

openssl pkcs12 -in cncpo-base64.pfx -out cncpo.pem  -clcerts -nodes

### Credits

The original tool [kit-censura](https://github.com/rfc1036/kit-censura) was written by Marco d'Itri <md@Linux.IT> [@rfc1036](https://github.com/rfc1036)  
