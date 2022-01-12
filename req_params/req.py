from urllib.parse import parse_qs, urlencode, urlparse

if __name__ == '__main__':
    
    # querystring = "http://www.youtube.com/watch?sock=Red&colour=Blue&size=large"
    querystring = "sock=Red&colour=Blue&size=large"

    print (querystring)
    
    # Parse request query string to get js object
    params = {k : v[0] for k, v in parse_qs(querystring.lower()).items()}
    print(parse_qs(querystring.lower()).items())
    
    for key, value in params.items():
      print("For %s user submitted %s" % (key, value))
    
    # Sort param keys
    sortedParams = sorted(params.items(), key=lambda x: x[0])

    # Update request querystring with normalized
    querystring = urlencode(sortedParams)
    
    print ('new querystring is', querystring)
    
    parsed_url = urlparse('http://www.youtube.com/watch?sock=Red&colour=Blue&size=Large'.lower())
    q = parse_qs(parsed_url.query) # there's also 
    # print(parsed_url)
    # ParseResult(scheme='http', netloc='www.youtube.com', path='/watch', 
    #   params='', query='?sock=Red&colour=Blue&size=large', fragment='')
    print('parsed_url query', q)
    # print('encoded url', urlunparse(q))
    print('original url in lc', parsed_url.geturl())
