
bidders = {}
status = True
def highestBidder(bidDictionary):
    highestBid = 0
    winner = ""
    for bidder in bidDictionary:
        bid_amount = bidDictionary[bidder]
        if(bid_amount > highestBid):
            highestBid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highestBid}")


while(status):
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    answer = input("Are there any other bidders? Type 'yes' or 'no'")
    bidders[name] = bid
    if(answer == "no"):
        status = False
        highestBidder(bidders)


