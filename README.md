**EdgePointsCollector: An App to Earn Points in Microsoft Edge**  
_Use your points to redeem cool rewards like RP for League of Legends or online store discounts!_

---

**Hello there!**

Before using the **EdgePointsCollector** app, it's a good idea to save your work to avoid losing any important data, as the app will close your browser.

If you want to quickly earn points from Microsoft Edge, this app is for you.

Here’s an example:  

**Important**:

1. You need to be logged into your Microsoft account to earn points.

2. Please note that you can only earn **90 points per day**. It’s not a lot, but if you use this app every day for a year, you will accumulate quite a bit! Additionally, you can complete the daily set offered by Microsoft on their site:
<br>
[Microsoft Rewards](https://rewards.bing.com/).
![image](https://github.com/user-attachments/assets/b3c23fd5-154e-4287-97d1-d2e85f0332b0)

3. If the app doesn’t work as expected, you might need to adjust some settings. Follow these steps:

   a. Find the **Microsoft Edge** application on your computer and open its **Properties**.  
   b. In the **Properties** window, locate the "Target" field.  
   c. Copy the contents of the "Target" field and update the file path in line 15 in the code as shown below:

```app = "!!!hereAddYourTarget!!!"```


If your PC or internet connection is fast, you can adjust the `time.sleep` property to **10** or **20** seconds. Run the program a few times to determine the optimal timing for you.  
However, if your computer or internet is slow, you might need to increase the `time.sleep` duration to **30** or **40** seconds, or even longer, if necessary.

The app will open new tabs after the process, allowing you to see how many points you’ve earned.  
**Pro Tip**: It's recommended to clear your browsing history from the last hour in Edge, as this app will flood your history with browsing data, like the one shown below. Don't worry, the app will open a "clear history" tab for you. 😅
![image](https://github.com/user-attachments/assets/80132b23-b9f3-41df-a921-d3d74fea2987)

---

**Enjoy earning points, everyone!** 😄
