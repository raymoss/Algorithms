int height_binary_tree(node* node, int height){
    if (!node)
        return height;
    else{
        int height_left = height_binary_tree(node->left, height + 1);
        int height_right = height_binary_tree(node->right, height + 1);
        return max(height_left, height_right);
    }
}