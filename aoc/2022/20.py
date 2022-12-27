from tqdm import tqdm


class ListNode:
    def __init__(self, val, prev, next):
        self.val = val
        self.prev = prev
        self.next = next


def shift(target, size):
    n = (-1 if target.val < 0 else 1) * (abs(target.val) % (size - 1))
    if n == 0:
        return

    # extract target
    target.prev.next = target.next
    target.next.prev = target.prev

    # find insertion point
    ins = target
    for _ in range(abs(n) + int(n < 0)):
        if n > 0:
            ins = ins.next
        else:
            ins = ins.prev

    # insert target
    target.next = ins.next
    target.prev = ins
    ins.next.prev = target
    ins.next = target


def mix(nums, num_mixes=1):
    # create list
    root = curr = ListNode(nums[0], None, None)
    nodes = [root]
    for n in nums[1:]:
        curr.next = ListNode(n, curr, None)
        curr = curr.next
        nodes.append(curr)
    curr.next = root
    root.prev = curr

    # perform shifts
    for _ in tqdm(range(num_mixes)):
        for node in nodes:
            shift(node, len(nums))

    return root


def decrypt(num_mixes=1, decryption_key=1):
    with open('scratch.txt') as f:
        nums = [int(n) * decryption_key for n in f.read().split('\n')]
        mixed = mix(nums, num_mixes)
        curr = mixed
        while curr.val != 0:
            curr = curr.next
        coord_sum = 0
        for _ in range(3):
            for _ in range(1000):
                curr = curr.next
            coord_sum += curr.val
        return coord_sum


print(decrypt())  # Part 1
print(decrypt(10, 811589153))  # Part 1
