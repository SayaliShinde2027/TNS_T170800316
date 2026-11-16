def parse_request(request):
    first_line = request.split("\n")[0]
    url = first_line.split(" ")[1]

    http_pos = url.find("://")
    if http_pos != -1:
        url = url[(http_pos+3):]

    port = 80
    port_pos = url.find(":")
    path_pos = url.find("/")

    if path_pos == -1:
        path_pos = len(url)

    if port_pos == -1 or path_pos < port_pos:
        host = url[:path_pos]
    else:
        host = url[:port_pos]
        port = int(url[port_pos+1:path_pos])

    return host, port, url