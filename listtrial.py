special_guest = ['james'.title(), 'emmanuel'.title(), 'lawrence'.title(), 'jennifer'.title(), 'uncle'.title()]
print(special_guest)

vip_guest = ['jennifer'.title(), 'emmanuel'.title(), 'james'.title()]
print(vip_guest)

real_friends = 'jennifer'
print("\nPlease " + real_friends.title() + " can you make it to my birthday party?" + ".")

real_friends = 'emmanuel'
print("\nPlease " + real_friends.title() + " can you make it to my birthday party?" + ".")

real_friends = 'james'
print("\nPlease " + real_friends.title() + " can you make it to my birthday party?" + ".")

vip_guest = ['jennifer'.title(), 'emmanuel'.title(), 'james'.title(), 'uncle'.title()]
print(vip_guest)

del vip_guest[3]
print(vip_guest)

vip_guest.insert(3, 'lawrence'.title())
print(vip_guest)



real_friends = 'lawrence'
print("\nPlease " + real_friends.title() + " can you make it to my birthday party?" + ".")


print(vip_guest)
print("I just found a bigger dinner table, so now space is available" + ".")

vip_guest.insert(0, 'chuba'.title())
vip_guest.insert(3, 'zeddy'.title())
vip_guest.insert(7, 'chibike'.title())
print(vip_guest)

real_friends = 'chuba'
print("\nPlease " + real_friends.title() + " can you make it to my birthday party?" + ".")
real_friends = 'zeddy'
print("\nPlease " + real_friends.title() + " can you make it to my birthday party?" + ".")
real_friends = 'chuba'
print("\nPlease " + real_friends.title() + " can you make it to my birthday party?" + ".")
print(vip_guest)
print("I'm sorry guys, i can only afford inviting two people")

popped_vip_guest = vip_guest.pop(0)
print(popped_vip_guest + " I am sorry i can't invite you to dinner again")
popped_vip_guest = vip_guest.pop(4)
print(popped_vip_guest + " I am sorry i can't invite you to dinner again")
popped_vip_guest = vip_guest.pop(4)
print(popped_vip_guest + " I am sorry i can't invite you to dinner again")


print(vip_guest)

popped_vip_guest = vip_guest.pop(0)
print(popped_vip_guest + " you are still invited for my birthday")

popped_vip_guest = vip_guest.pop(1)
print(popped_vip_guest + " you are still invited for my birthday")

popped_vip_guest = vip_guest.pop(-2)
print(popped_vip_guest + " you are still invited for my birthday")

popped_vip_guest = vip_guest.pop(-1)
print(popped_vip_guest + " you are still invited for my birthday")

vip_guest = ['jennifer'.title(), 'emmanuel'.title(), 'james'.title(), 'uncle'.title()]
print(vip_guest)

del vip_guest[3]
del vip_guest[2]
del vip_guest[1]
del vip_guest[0]
print(vip_guest)