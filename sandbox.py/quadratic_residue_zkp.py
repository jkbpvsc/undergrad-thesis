import random

class Prover:
    def __init__(self, secret, modulo):
        self.secret = secret
        self.modulo = modulo

    def start_round(self):
        u = random.randrange(0, self.modulo)
        self.u = u

        #print("Prover: Starting round\nProver: Picking random u:", u)

        return (u ** 2) % self.modulo

    def respond_to_coin_toss(self, coin_toss):
        if coin_toss == 0:
            return self.u
        elif coin_toss == 1:
            return (self.secret * self.u) % modulo

class Verifier:
    def __init__(self, secret_q_res, modulo):
        self.secret_q_res = secret_q_res
        self.modulo = modulo

    def toss_coin(self, y):
        self.y = y
        self.coin_toss = random.getrandbits(1)

        print("Verifier: Coin toss:", self.coin_toss)

        return self.coin_toss

    def verify_respons(self, response):
        if self.coin_toss == 0:
            return (response ** 2) % self.modulo == self.y % self.modulo
        else:
            return (response ** 2) % self.modulo == (self.secret_q_res * self.y) % self.modulo
    

if __name__ == "__main__":
    rounds = 32
    secret = int.from_bytes(bytearray("Super secret", "utf8"), "big")
    incorrect_secret = int.from_bytes(bytearray("Fake password", "utf8"), "big")

    modulo = 997
    prover = Prover(secret, modulo)

    secret_q_res = (secret ** 2) % modulo
    verifier = Verifier(secret_q_res, modulo)

    for i in range(rounds):
        y = prover.start_round()
        coin_toss = verifier.toss_coin(y)
        z = prover.respond_to_coin_toss(coin_toss)
        verification_response = verifier.verify_respons(z)

        #print("Validation: ", verification_response)
        
        if not verification_response:
            print("Validation failed")
            break
        else:
            percent = 100 - (2 ** ((i+1) * -1) * 100)
            print("Validation succeded, with %8.6f%% confidence" % (percent))




