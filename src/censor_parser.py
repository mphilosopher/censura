#!/usr/bin/env python3

import optparse
import csv

options = None
default_blackhole = '127.0.0.1'
default_bind_block_zonefile = '/etc/bind/zones/dns_block_zone.zone'
out_format_list = ['unbound', 'bind']
in_format_list = ['cncpo', 'aams', 'admt', 'manuale']

def write_unbound_list(outfile, blacklist, blackhole):
    fp = open(outfile, 'w')
    fp.write("server:\n")
    for c in blacklist:
        fp.write("local-zone: \"{}\" redirect \n".format(c))
        fp.write("local-data: \"{} A {}\"\n".format(c, blackhole))
    fp.close()
    return


def write_bind_data(outfile, blacklist, zonefile):
    fp = open(outfile, 'w')
    for c in blacklist:
        fp.write('zone "{}" {{ type master; file "{}"; }};\n'.format(c, zonefile))
    fp.close()
    return


def parse_cncpo_list(infile):
    black_list = list()
    i = 0

    csvfile = open(infile)
    spamreader = csv.reader(csvfile, delimiter=';')
    for row in spamreader:
        if i == 0:
            i = 1
            continue
        if row is not None and len(row)>0 :
            data = row[1].strip()
            if len(data) > 0:
                black_list.append(data)
    csvfile.close()
    # Eliminazione dei duplicati
    bl2 = list(set(black_list))
    return bl2


def parse_aams_list(infile):
    black_list = list()
    fp = open(infile)
    line = fp.readline()
    while line:
        data = line.strip()
        if len(data) > 0:
                black_list.append(data)
        line = fp.readline()
    fp.close()
    # Eliminazione dei duplicati
    bl2 = list(set(black_list))
    return bl2


def parse_manual_list(infile):
    black_list = list()
    fp = open(infile)
    line = fp.readline()
    while line:
        data = line.strip()
        if len(data) > 0:
            black_list.append(data)
        line = fp.readline()
    fp.close()
    # Eliminazione dei duplicati
    bl2 = list(set(black_list))
    return bl2


def main():
    global options
    dns_bl = None

    # Elaborazione argomenti della linea di comando
    usage = "usage: %prog [options] arg"
    parser = optparse.OptionParser(usage)
    parser.add_option("-i", "--input", dest="in_file", help="File di elenco degli url in input")
    parser.add_option("-o", "--output", dest="out_file", help="File di output generato")
    parser.add_option("-b", "--blackhole", dest="blackhole", help="Indirizzo stop-page/blackhole")
    parser.add_option("-f", "--oformat", dest="out_format", help="Formato dns in output (unbound, bind)")
    parser.add_option("-d", "--iformat", dest="in_format", help="Formato dns in output (unbound, bind)")
    parser.add_option("-z", "--zonefile", dest="bind_zonefile", help="Pathname del file di zona bind di blocco")
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet", action="store_false", dest="verbose")

    (options, args) = parser.parse_args()
    if len(args) == 1:
        parser.error("Numero di argomenti non corretto")
    if (options.in_file is None) or ( options.out_file is None):
        parser.error("Numero di argomenti non corretto")
    if (options.out_format is None) or not (options.out_format in out_format_list):
        parser.error("Formato di output errato")
    if (options.in_format is None) or not (options.in_format in in_format_list):
        parser.error("Formato di input errato")
    if options.verbose:
        print("File di input       : {}".format(options.in_file))
        print("File di output      : {}".format(options.out_dir))
        print("Formato             : {}".format(options.out_format))
    #
    if options.blackhole is None:
            options.blackhole = default_blackhole
    if options.bind_zonefile is None:
            options.bind_zonefile = default_bind_block_zonefile
    #
    if options.in_format == 'cncpo':
        dns_bl = parse_cncpo_list(options.in_file)
    elif options.in_format == 'aams':
        dns_bl = parse_aams_list(options.in_file)
    elif options.in_format == 'admt':
        dns_bl = parse_aams_list(options.in_file)
    elif options.in_format == 'manuale':
        dns_bl = parse_manual_list(options.in_file)
    else:
        print("Formato di input non risconosciuto")
        return None
    if options.out_format == 'unbound':
        write_unbound_list(options.out_file, dns_bl, options.blackhole)
    elif options.out_format == 'bind':
        write_bind_data(options.out_file, dns_bl, options.bind_zonefile)
    else:
        print("Formato di output non risconosciuto")
        return None
    return

if __name__ == '__main__':
    main()
