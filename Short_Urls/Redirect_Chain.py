import requests
url=raw_input()
def get_chain(url):
    try:
        r = requests.get(url)
        #print "Processing " + url
        if len(r.history) > 0:
            print r.history
            chain = ""
            code = r.history[0].status_code
            #print code
            final_url = r.url
            for resp in r.history:
                chain += resp.url + " | "
            #print final_url
            #print chain
            return str(code) + '\t' + str(len(r.history)) + '\t' + chain + '\t' + final_url + '\t'
        else:
            return str(r.status_code) + '\t\t\t\t'
    except requests.ConnectionError:
        print("Error: failed to connect.")
        return '0\t\t\t\t'

k = get_chain(url)
print k
# input_file = 'C:\Users\KC-L\Documents\\bit.do.txt'
# output_file = 'C:\Users\KC-L\Documents\output.txt'

# with open(output_file, 'w') as o_file:
#     o_file.write('URL\tStatus\tNumber of redirects\tRedirect Chain\tFinal URL\t\n')
#     f = open(input_file, "r")
#     lines = f.read().splitlines()
#     for line in lines:
#         code = get_status_code(line)
#         o_file.write(line + "\t" + str(code) + "\t\n")
# f.close()