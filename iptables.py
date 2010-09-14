from django.template import Context, Template
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

def generate_iptables_from_file(output_file, input_file):
    f = open(input_file, 'r')
    ips = [line.rstrip() for line in f if line.rstrip()] # rm newlines
    generate_iptables(output_file, ips)

def generate_iptables(filename, ips):
    """
        Generate iptables files from templates.
    """
    print("Generating iptables file:\n")
    print("-----------")
    f = open('templates/%s' % filename)
    f = ''.join([line for line in f])
    t = Template(f)    
    c = Context({ 'servers': ips })
    rendered = t.render(c)

    out = open('rendered/%s' % filename, 'w')
    out.write(rendered)
    print(rendered)
    print("-----------")
    print("\nThe file was written to rendered/%s" % filename)

if __name__ == "__main__":
    generate_iptables_from_file('iptables.int.rules', 'ips.txt')
