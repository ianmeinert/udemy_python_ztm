is_magician = False
is_expert = True

# check if magician AND expert: "you are a master magician"
if is_magician and is_expert:
    print("you are a master magician")
# check if magician but not expert: "at least you're getting there"
elif is_magician and not is_expert:
    print("at least you're getting there")
# if you're not a magician: "you need magic powers"
elif not is_magician:
    print("you need magic powers")
