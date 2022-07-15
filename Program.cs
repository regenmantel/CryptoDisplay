using Newtonsoft.Json;
using RestSharp;
using System;

namespace CryptoDisplay
{
    public class Program
    {
        

        static string[] cryptoList = { "BTC", /*"ETH", "DOGE", "ALICE", "SHIB", "HOT", "AMP"*/ };
        static double btc_old = 1;
        static double btc_new = 1;
        static double btc = 0;
        public static void Main(string[] args)
        {
            var startTimeSpan = TimeSpan.Zero;
            var periodTimeSpan = TimeSpan.FromMinutes(1);

            var timer = new System.Threading.Timer((e) =>
            {
                getCryptoInfo();
            }, null, startTimeSpan, periodTimeSpan);

            Console.ReadLine();
        }

        public static void getCryptoInfo()
        {
            var client = new RestClient("https://rest.coinapi.io/v1/assets");
            var request = new RestRequest(Method.GET);

            request.AddHeader("X-CoinAPI-Key", "24A5848F-BF26-4DDD-8DE8-3284D21B36E3");
            IRestResponse response = client.Execute(request);

            var inf = JsonConvert.DeserializeObject<dynamic>(response.Content);

            Console.WriteLine("\nKURS: " + DateTime.Now + "\n");
            foreach (var item in inf)
            {
                for (int i = 0; i < cryptoList.Length; i++)
                {
                    if (item["asset_id"] == cryptoList[i])
                    {
                        btc_new = item.price_usd;

                        //Console.WriteLine("BTC old: " + btc_old);
                        //Console.WriteLine("BTC new: " + btc_new);

                        if (btc_old > 1) 
                            if (item["asset_id"] == "BTC")
                                btc = (btc_new / btc_old - 1) * 100;
                    
                        //Console.WriteLine("BTC %: " + btc);

                        Console.WriteLine("{0,-10} {1,-8} ${2-10:0.00} {3:+0.00;-0.00}%", item.name, item.asset_id, item.price_usd, btc);
                    }

                    btc_old = btc_new;
                }
            }
        }
    }
}
