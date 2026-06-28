public class Node{
    Node links[] = new Node[26];
    boolean flag=false;
}

class PrefixTree {
    private Node root;

    public PrefixTree() {
        root=new Node();
         
    }

    public void insert(String word) {

        Node cur =root;
        for (char c:word.toCharArray()){
            int i =c-'a';
            if (cur.links[i]==null){
                cur.links[i]=new Node();
            }
            cur=cur.links[i];
        }
        cur.flag=true;



    }

    public boolean search(String word) {

        Node cur=root;
        for(char c:word.toCharArray()){
            int i=c-'a';
            if (cur.links[i]== null){
                return false;
            }
            cur=cur.links[i];
        }
        return cur.flag;

    }

    public boolean startsWith(String prefix) {
        Node cur=root;
        for (char c:prefix.toCharArray()){
            int i=c-'a';
            if (cur.links[i]==null){
                return  false;
                
            }
            cur=cur.links[i];
        }
        return true;

    }
}
