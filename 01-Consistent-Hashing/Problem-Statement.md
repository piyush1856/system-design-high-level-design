# Problem Statement: Consistent Hashing with a Hash Ring

## Overview

We have a hash ring where we have locations available from 0 degrees to 359 degrees. Implement a consistent hashing in the following way: You can add a server to the hash ring. We just need to pass the serverID and the hash functions automatically assign them one location on the hash ring. The serverID can be strings.

## Operations

You can perform the following operations on the hash ring:

1. **ADD servername**: This will add the specified server to your hash ring.
2. **REMOVE servername**: This will remove the specified server from the hash ring.
3. **ASSIGN keyname**: This assigns an incoming request to one of the servers nearest to the name's hash location in a clockwise direction. If no server is found in the clockwise direction, pick the nearest server from 0 degrees in clockwise direction. If there are multiple servers at that location, assign the request to the latest server added.

### Guarantees

- It is guaranteed that all the key names and server names would be unique.
- At least one server exists for ASSIGN type requests.

## Input

You are given two string vectors A and B and an integer array C. For all valid i:

- A[i] tells you the type of operation of the i-th query.
- B[i] tells you the key/server name depending on the type of query.
- C[i] tells you the hashKey for the i-th operation.

### Operation Types

- **ADD**: B[i] is an uppercase string with 5 or more letters. They are all unique among add queries.
- **REMOVE**: B[i] is an uppercase string with 5 or more letters. They are all unique among remove queries.
- **ASSIGN**: B[i] is an uppercase string with exactly 4 letters. They are all unique among all queries.

### Constraints

- 1 <= A.size() <= 10^4 + 30
- 1 <= B.size() <= 10^4 + 30
- 1 <= C.size() <= 10^4 + 30
- A.size() = B.size() = C.size()

### Hash Function

You need to use the following hash function to assign degrees to servers/keys:

```python
def user_hash(username, hashKey):
    p = hashKey
    n = 360
    hashCode = 0
    p_pow = 1
    for character in username:
        hashCode = (hashCode + (ord(character) - ord('A') + 1) * p_pow) % n
        p_pow = (p_pow * p) % n
    return hashCode
