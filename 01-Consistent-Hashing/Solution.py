answers = []
server_location = {}
server_to_key_mappings = {}

class Solution:
    def user_hash(self, username, hash_key):
        p = hash_key
        n = 360
        hash_code = 0
        p_pow = 1
        for character in username:
            hash_code = (hash_code + (ord(character) - ord('A') + 1) * p_pow) % n
            p_pow = (p_pow * p) % n
        return hash_code

    def assign_key_to_server(self, key, key_hash):
        global server_location, server_to_key_mappings

        if not server_location :
            return -1

        key_hash_location = self.user_hash(key, key_hash)
        sorted_server_location = sorted(server_location.keys())

        # Finding nearest server to the key_hash_location
        for location in sorted_server_location :
            if location >= key_hash_location :
                server_name = server_location[location]

                if server_name not in server_to_key_mappings :
                    server_to_key_mappings[server_name] = []

                server_to_key_mappings[server_name].append((key, key_hash))
                return location

        # If no server found
        server_name = server_location[sorted_server_location[0]]

        if server_name not in server_to_key_mappings:
            server_to_key_mappings[server_name] = []

        server_to_key_mappings[server_name].append((key, key_hash))
        return sorted_server_location[0]

    def remove_server(self, server_name):
        global server_location, server_to_key_mappings

        for key, value in list(server_location.items()) :
            if value == server_name :
                del server_location[key]
                break

        keys_to_reassign = server_to_key_mappings.get(server_name, [])
        if server_name in server_to_key_mappings :
            del server_to_key_mappings[server_name]

        for key, key_hash in keys_to_reassign :
            self.assign_key_to_server(key, key_hash)

        return len(keys_to_reassign)

    def reassign_keys_after_server_addition(self, server_hash_location):
        global server_location, server_to_key_mappings

        if not server_to_key_mappings :
            return

        clockwise_server_location = sorted(server_location.keys())

        # Finding key around clockwise
        for location in clockwise_server_location :
            if location > server_hash_location :
                server_name = server_location[location]
                keys_to_reassign = server_to_key_mappings.get(server_name, [])
                server_to_key_mappings[server_name] = []

                for key, key_hash in keys_to_reassign:
                    self.assign_key_to_server(key, key_hash)
                return

        # If no closer server found, means location of new server is farthest
        # we have to reassign first server keys again
        first_server_name = server_location[clockwise_server_location[0]]
        keys_to_reassign = server_to_key_mappings.get(first_server_name, [])
        server_to_key_mappings[first_server_name] = []

        for key, key_hash in keys_to_reassign:
            self.assign_key_to_server(key, key_hash)
        return

    def add_server(self, server_name, key):
        global server_location, server_to_key_mappings

        server_hash_location = self.user_hash(server_name, key)
        server_location[server_hash_location] = server_name
        self.reassign_keys_after_server_addition(server_hash_location)
        return len(server_to_key_mappings.get(server_name, []))

    def handleOperation(self, operation, name, key):
        global answers
        if operation == "ADD":
            answers.append(self.add_server(name, key))
        elif operation == "REMOVE":
            answers.append(self.remove_server(name))
        elif operation == "ASSIGN":
            answers.append(self.assign_key_to_server(name, key))

    def solve(self, operations, names, keys):
        global server_location, server_to_key_mappings, answers
        server_to_key_mappings.clear()
        server_location.clear()
        answers = []

        for i in range(len(operations)):
            self.handleOperation(operations[i], names[i], keys[i])

        return answers

if __name__ == '__main__':
    solution = Solution()

    A = ["ADD", "ASSIGN", "ADD", "ASSIGN", "REMOVE", "ASSIGN"]
    B = ["INDIA", "NWFJ", "RUSSIA", "OYVL", "INDIA", "IGAX"]
    C = [7, 3, 5, 13, -1, 17]
    print(solution.solve(A, B, C))
