/**
 * 旅行商问题
 * Created by devin on 15-11-13.
 */
public class TSP {

    private static int N = 4;

    private int cl; //当前路径的长度
    private int fl; //当前只当的最大路径长度

    private int weight[][] = {
            {0, 30, 6, 5},
            {30, 0, 4, 10},
            {6, 4, 0, 20},
            {5, 10, 20, 0}
    };
    private int x[] = new int[4];

    public int[] getX(){
        return x;
    }
    /**
     * 判断第k个数是否不同与前k-1个数
     * @param k
     * @return bool
     */
    private boolean nextValue(int k){
        int i = 0;
        while(i < k){
            if(x[k] == x[i]){
                return false;
            }
            i += 1;
        }
        return true;
    }

    public void solve(){
        int k = 1;
        cl = 0;
        fl = Integer.MAX_VALUE;

        while(k > 0){
            x[k] = Math.floorMod(x[k] + 1, N);
            for(int j=0;j < N;j++){ //最左n次 必定有个没有设置
                if(nextValue(k)){
                    cl += weight[x[k-1]][x[k]];
                    break;
                }
                x[k] = Math.floorMod(x[k] + 1, N);
            }
            if(fl <= cl || k == N-1 && fl < cl+weight[x[k]][0]){
                cl = cl - weight[x[k-1]][x[k]] ;
                k -= 1; //回溯
            }else if(k == N-1 && fl >= cl+weight[x[k]][0]){
                fl = cl + weight[x[k]][0];
                cl = cl - weight[x[k-1]][x[k]] ;
                k -= 1; //回溯
            }else{
                k = k + 1; //继续搜索
            }
            System.out.println("k:"+ k + ",fl:" + fl + ",cl:"+cl);
        }
        System.out.println("end");
    }

}
