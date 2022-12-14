#from replit import clear
#Need to figure out the clear screen part

from art import logo

print(logo)

print("Welcome to blind auction program.\n")


def auction(fresh_name, fresh_bid):
    """This function is used to add names of new bidders"""
    new_bids = {}
    new_bids[fresh_name] = fresh_bid
    bids.update(new_bids)


bids = {}
is_continue = True

while is_continue:
    fresh_name = input("What is your name?\n")
    fresh_bid = input("What is your bid?\n")
    auction(fresh_name, fresh_bid)
    more = input("Are there any more bidders? Enter 'yes' or 'no'.\n")
    clear()
    #Need to figure out the clear screen part
    if more == "no":
        is_continue = False

check = ""
previous_bid = 0
for check in bids:
    if (int(bids[check])) > previous_bid:
        previous_bid = int(bids[check])
        highest_bidder = check

print(f"The highest bidder is {highest_bidder}, with a bid of ${previous_bid}.")
