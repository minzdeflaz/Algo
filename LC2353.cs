//https://leetcode.com/problems/design-a-food-rating-system/
/*
Tasks:
modify food ratings
return HighestRated

cuisine dictionary: {cuisine: {food: rating}}
cuisine top dictionary: {cuisine : max_heap}
*/


public class FoodRatings {
    private Dictionary<string, int> food_to_ratings = new();
    private Dictionary<string, string> food_to_cuisine = new();
    private Dictionary<string, PriorityQueue<(string, int), (int, string)>> top_cuisine_map = new();
    public FoodRatings(string[] foods, string[] cuisines, int[] ratings) {
        for (int i=0; i<foods.Length; i++) {
            food_to_ratings[foods[i]] = ratings[i];
            food_to_cuisine[foods[i]] = cuisines[i];
            
            if (!top_cuisine_map.ContainsKey(cuisines[i])){
                top_cuisine_map[cuisines[i]] = new();
            }

            top_cuisine_map[cuisines[i]].Enqueue((foods[i], ratings[i]), (-ratings[i], foods[i]));
        }
    }
    
    public void ChangeRating(string food, int newRating) {
        food_to_ratings[food] = newRating;
        var cuisine = food_to_cuisine[food];
        top_cuisine_map[cuisine].Enqueue((food, newRating), (-newRating, food));

    }
    
    public string HighestRated(string cuisine) {
        (var top_food, var rating) = top_cuisine_map[cuisine].Peek();

        while (rating != food_to_ratings[top_food]){
            top_cuisine_map[cuisine].Dequeue();
            (top_food, rating) = top_cuisine_map[cuisine].Peek();
        }

        return top_food;
    }
}
#region Use Custom Comparer
// public class CusComparer : IComparer<ValueTuple<string, int>> {
//     public int Compare (ValueTuple<string, int> tup1, ValueTuple<string, int> tup2){
//         if (tup1.Item2 == tup2.Item2){
//             return tup1.Item1.CompareTo(tup2.Item1);
//         } else {
//             return tup2.Item2.CompareTo(tup1.Item2);
//         }
//     }
// }

// public class FoodRatings {
//     private Dictionary<string, int> food_to_ratings = new();
//     private Dictionary<string, string> food_to_cuisine = new();
//     private Dictionary<string, PriorityQueue<(string, int), (string, int)>> top_cuisine_map = new();
//     public FoodRatings(string[] foods, string[] cuisines, int[] ratings) {
//         for (int i=0; i<foods.Length; i++) {
//             food_to_ratings[foods[i]] = ratings[i];
//             food_to_cuisine[foods[i]] = cuisines[i];
            
//             if (!top_cuisine_map.ContainsKey(cuisines[i])){
//                 top_cuisine_map[cuisines[i]] = new(new CusComparer());
//             }

//             top_cuisine_map[cuisines[i]].Enqueue((foods[i], ratings[i]), (foods[i], ratings[i]));
//         }
//     }
    
//     public void ChangeRating(string food, int newRating) {
//         food_to_ratings[food] = newRating;
//         var cuisine = food_to_cuisine[food];
//         top_cuisine_map[cuisine].Enqueue((food, newRating), (food, newRating));

//     }
    
//     public string HighestRated(string cuisine) {
//         (var top_food, var rating) = top_cuisine_map[cuisine].Peek();

//         while (rating != food_to_ratings[top_food]){
//             top_cuisine_map[cuisine].Dequeue();
//             (top_food, rating) = top_cuisine_map[cuisine].Peek();
//         }

//         return top_food;
//     }
// }
#endregion
/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings obj = new FoodRatings(foods, cuisines, ratings);
 * obj.ChangeRating(food,newRating);
 * string param_2 = obj.HighestRated(cuisine);
 */