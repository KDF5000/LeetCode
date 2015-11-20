/**
 * Created by devin on 15-11-13.
 */
public class Main {
    public static void main(String[] args){
        //n皇后
//        NQueue nq = new NQueue(4);
//        nq.solve();
//        int[] a = nq.getX();
//        for(int i : a){
//            System.out.println(i);
//        }
        //tsp
//        BackTsp tsp = new BackTsp();
//        tsp.solve();
//        int b[] =tsp.getX();
//        for(int i : b){
//            System.out.println(i);
//        }
        BackTSP tsp = new BackTSP();
        tsp.solve();
        int b[] =tsp.getBestX();
        for(int i : b){
            System.out.println(i);
        }
        System.out.println("最优路径长度:" + tsp.getMinLen());


    }
}
