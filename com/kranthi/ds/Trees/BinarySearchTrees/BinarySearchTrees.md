<h1>Binary Search Trees</h1>
<p>
Binary Search Tree is a node-based binary tree data structure which has the following properties:

- The left subtree of a node contains only nodes with keys lesser than the node’s key.
- The right subtree of a node contains only nodes with keys greater than the node’s key.
- The left and right subtree each must also be a binary search tree.</p>

<p>
Binary Search Tree, is a node-based binary tree data structure which has the following properties:
The left subtree of a node contains only nodes with keys lesser than the node’s key.
The right subtree of a node contains only nodes with keys greater than the node’s key.
The left and right subtree each must also be a binary search tree.
There must be no duplicate nodes.
</p>
<h3>Searching a key</h3>
<p>
For searching a value, if we had a sorted array we could have performed a binary search. Let’s say we want to search 
a number in the array what we do in binary search is we first define the complete list as our search space, the number 
can exist only within the search space. Now we compare the number to be searched or the element to be searched with the 
mid element of the search space or the median and if the record being searched is lesser we go searching in the left 
half else we go searching in the right half, in case of equality we have found the element. In binary search we start 
with ‘n’ elements in search space and then if mid element is not the element that we are looking for, we reduce the 
search space to ‘n/2’ and we go on reducing the search space till we either find the record that we are looking for or 
we get to only one element in search space and be done with this whole reduction.

Search operation in binary search tree will be very similar. Let’s say we want to search for number, 
what we’ll do is we’ll start at root and then we will compare the value to be searched with value of root if it’s equal 
we are done with the search if it’s lesser we know that we need to go to the left subtree because in a binary search 
tree all the elements in the left subtree are lesser and all the elements in right subtree are greater. Searching an 
element in the binary search tree is basically this traversal in which at each step we will go either towards left or 
right and hence in at each step we discard one of the sub-trees. If the tree is balanced, we call a tree balanced if 
for all nodes the difference between the heights of left and right subtrees is not greater than one, we will start with 
a search space of ‘n’nodes and when we will discard one of the sub-trees we will discard ‘n/2’ nodes so our search space
 will be reduced to ‘n/2’ and then in the next step we will reduce the search space to ‘n/4’ and we will go on reducing 
 like this till we find the element or till our search space is reduced to only one node. The search here is also a 
 binary search and that’s why the name binary search tree.
</p>
<p>
<h3>Insertion of a key</h3>
A new key is always inserted at leaf. We start searching a key from root till we hit a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node.

         100                               100
        /   \        Insert 40            /    \
      20     500    --------->          20     500 
     /  \                              /  \  
    10   30                           10   30
                                              \   
                                              40
</p>