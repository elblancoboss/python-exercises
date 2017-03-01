"""For this exercise you are called to develop a simple Case-Based Reasoning Algorithm

Overview: 

You are to develop a RECOMMENDER SYSTEM in python based on Case-Based Reasoning technology with a similarity metric. The cases will contain products with 4 random features, prices, and also an informal rating for these products (6 features overall). 

You should be able to demonstrate:
1.	A similarity function. When two cases can be marked as similar? E.g. 100% similarity vs. 0%. Which similarity method could you use? (HINT: You may want to use Euclidean distance or Manhattan similarity, or any other suitable metric for recommender systems)
2.	Have a method to add cases. Cases can be stored in either lists or dictionaries
3.	Demonstrate a scenario where a new case enter your system. You should be able to calculate its similarity vs. any existing cases and present the 3 nearest ones. Based on their ratings or prices you should be able to predict a rating or price for the new case
4.	Propose alternative methods of expert systems development or any other techniques

Hint: This is a demanding exercise that requires some research and experimentation. In case you implement it successfully, feel free to use this work for your coursework and combine it with an application of your choice.

Hint 2: Give emphasis on concept and code clarity and comments. Feel free to provide extra comments or examples of your code usage."""

phone = { "Apple": {'Name': 'iPhone 7', 'Colour': 'white', 'Megapixels': 20, 'Price': 800, "Storage": 128, "Rating": 5},
          "Sony": {'Name': 'Xperia X5', 'Colour': 'black', 'Megapixels': 15, 'Price': 700, "Storage": 64, "Rating": 4},
          "Samsung": {'Name': 'Galaxy S7', 'Colour': 'silver','Megapixels': 10, 'Price': 600, "Storage": 32, "Rating": 3},
          "Nokia": {'Name': 'Nokia 3310', 'Colour': 'white', 'Megapixels': 5, 'Price': 500, "Storage": 16, "Rating": 2}
      }
      
for company in phone:
    print ("\n",company,"\n Specs\n", )
    for version in phone[company]:
        print (version,':',phone[company][version])
        
storage_input = int(input("\nEnter storage amount: "))
camera_input = int(input("Enter camera megapixels: "))

diff = float('inf')
device_p = ""
for key, value in phone.items():
  for key_a, storage in value.items():
    if key_a == "Storage":
      if diff > abs(storage_input-storage):
          diff = abs(storage_input-storage)
          x = storage
          device_p = key
print ("\n", x)

diff = float('inf')
device_c = ""
for key, value in phone.items():
  for key_b, camera in value.items():
    if key_b == "Megapixels":
      if diff > abs(camera_input-camera):
          diff = abs(camera_input-camera)
          z = camera
          device_c = key
print (z)

print(device_p, ", Cost = ", phone[device_p]["Price"], ", Rating = ", phone[device_p]["Rating"])
print(device_c, ", Cost = ", phone[device_c]["Price"], ", Rating = ", phone[device_c]["Rating"])           

mid_1 = [phone[device_p]["Price"], phone[device_p]["Rating"]]
mid_2 = [phone[device_c]["Price"], phone[device_c]["Rating"]]

sum_1 = mid_1[0]+mid_2[0]
price = sum_1/2

sum_2 = mid_1[1]+mid_2[1]
rating = sum_2/2

estimate = price, rating
print ("Estimate price and rating", estimate)
