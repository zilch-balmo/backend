1. Given a token

2. Find key id in token headers
```
from jose import jwt
jwt.get_unverified_headers(token)
```

3. Get keys from amazon
```
# https://cognito-idp.{region}.amazonaws.com/{userPoolId}/.well-known/jwks.json
keys = get("https://cognito-idp.us-west-2.amazonaws.com/us-west-2_kVyMu9Hd9/.well-known/jwks.json").json()

{'keys': [{'alg': 'RS256',
   'e': 'AQAB',
   'kid': 'r899615+Fnq99mxEQws+/94bxVPPb0yhmt4ZhJQ7KdQ=',
   'kty': 'RSA',
   'n': '4GO1idJEnufBeg-TQ_NCwC4I35ySNnRBVf_YhzizjbJfEZ4sGML95vEeOIwElUXNvORUHHkPyS4xyUZZbSjzmpuy06Z1hiYavtxmzrgzSAw_X9-Gngpe5cGXeAOSt8Z8SO-toKTWz1_gYM4yjaUu09MjkF-IhLQLGfOCA90tEWpTKspyOR7PKllhGQX_0GB2AVpqSZ2tI-Z3YY48eZyd40ru2LhmmjtrGf54O8sVl87foL6LDIXZ6Ihl3miBIdiaoPwcCcXmDFRJcuXlILgUdQ9QqnY2o8NG2YhTYGR_hwRuTp9RouJke11vwf5IVmRg5FKU-IBWLjWK3jqtQYiqVw',
   'use': 'sig'},
  {'alg': 'RS256',
   'e': 'AQAB',
   'kid': '99kvKyXp1wAVfL1fWdEYM5rD72vgK42Af4yHe6T6yVc=',
   'kty': 'RSA',
   'n': 'jmRS-2eDa6AjyzF9pTzp9_MVDaBEKoKurEKCEwsEoNfxdtnf-RLfG-2XyavZBn2uR8oCBP3dW7xWdZQOP-Wnnm8Wbnhz4WqwfvhYwBpvTa5PQhg7XFZm0da2enr6FO6M5w4oJU1E5mW6Vob7UwFtyStMgMZkMp9F8KY3ybAKWw9900SjBgg0pbucYkmpxRQin75hoIWD0EAAm-j35mrLYFQOh8Po1Gp7Gh82gvDNHDcQTOUp5u3qhh-NHGJUrNrGmfqUXec1CQs8QI0xTE88EMy9AoK5q9Q4doemuZjUjgrfXfTIJyqI8gLqZrfxko8VPQFcqzxacOwk07j_1toweQ',
   'use': 'sig'}]}
```


4. Find key by key id

5. Decode token
```
claims = jwt.decode(token, k, algorithms=['RS256'])
```

6. Good gist: https://gist.github.com/richmondwang/b34ea009e5d102573cb111910212ea14

7. Library: https://github.com/mpdavis/python-jose
