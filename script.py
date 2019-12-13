class TreeNode:
    def __init__(self, story_piece):
        self.story_piece = story_piece
        self.choices = []

    def __repr__(self):
        return self.story_piece


story_root = TreeNode(
"""
You are in a forest clearing. There is a path to the left.
A bear emerges from the trees and roars!
Do you: 
1 ) Roar back!
2 ) Run to the left...
"""
)

print("Once upon a time...")
print(story_root)
