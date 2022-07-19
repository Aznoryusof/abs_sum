test_data1 = """
We refer to Mr Wee Gim Leong’s letter (Don't put employer's address on maid's work permit card, 30 May).

The Ministry of Manpower (MOM) has taken measures to make address information less visible on the Work Permit cards. Work Permit cards issued since 24 August 2020 no longer show the employer’s address. Migrant domestic workers (MDWs) who need to show proof of their residential addresses, e.g. to acquire services from service providers like banks and healthcare institutions, can retrieve their addresses through their SGWorkPass app instead. By July 2022, MDWs will be required to log in with their SingPass before their address information can be retrieved. There are also other ways to provide documentary proof of residential address, e.g. correspondences from MOM to the MDW.

To address the issue of MDWs borrowing from unlicensed moneylenders, it is important to educate MDWs on good money management practices and the risks of borrowing from unlicensed moneylenders. We do so through our Settling-in-Programme, regular newsletters, and courses that Non-Governmental Organisations conduct.

In addition, enforcement action will be taken against MDWs who borrow from unlicensed moneylenders, to deter them from doing so.
"""

test_data2 = """
#Person1#: Can I help you?\n#Person2#: Yes. I sent in my resume at the end of last week. I'm applying for the accounts assistant position.\n#Person1#: May I have your name please?\n#Person2#: My name is Judy Liao. That's spelled L I A O.\n#Person1#: Alright. . . And did you have some specific questions about your application?\n#Person2#: Not really. I was in the neighborhood, and I just wanted to stop in to see if you received my resume.\n#Person1#: Oh, that's no problem. Just give me a moment, and I can check. Judy Liao. Let's see. . . Yes, here it is. Judy Liao. We have received your resume.\n#Person2#: Thank you.\n#Person1#: Is there anything else I can help you with?\n#Person2#: Yes, maybe. The ad in the newspaper said you wanted the resume, a cover letter, and two letters of recommendation. I included those things in the envelope. Is there anything else I should send?\n#Person1#: No, that is all we need. If we have those things included, that is sufficient.\n#Person2#: Do you know when they will start setting up interviews for the job?\n#Person1#: I'm not really sure about that. But I know we are still receiving resumes. Maybe after a week or two they will start calling applicants.\n#Person2#: I see. Well, thank you very much for helping me. You have been very helpful.\n#Person1#: If you have any further questions, you can call any time.\n#Person2#: Thank you.\n#Person1#: Thank you. Goodbye.
"""

test_data2b = """
Can I help you? Yes. I sent in my resume at the end of last week. I'm applying for the accounts assistant position. May I have your name please? My name is Judy Liao. That's spelled L I A O. Alright. . . And did you have some specific questions about your application? Not really. I was in the neighborhood, and I just wanted to stop in to see if you received my resume. Oh, that's no problem. Just give me a moment, and I can check. Judy Liao. Let's see. . . Yes, here it is. Judy Liao. We have received your resume. Thank you. Is there anything else I can help you with? Yes, maybe. The ad in the newspaper said you wanted the resume, a cover letter, and two letters of recommendation. I included those things in the envelope. Is there anything else I should send? No, that is all we need. If we have those things included, that is sufficient. Do you know when they will start setting up interviews for the job? I'm not really sure about that. But I know we are still receiving resumes. Maybe after a week or two they will start calling applicants. I see. Well, thank you very much for helping me. You have been very helpful. If you have any further questions, you can call any time. Thank you. Thank you. Goodbye.
"""


test_data2_summary = """
Judy Liao's applying for the accounts assistant position. She asks #Person1# whether they have received her resume, and #Person1# helps her check. #Person1# tells Judy there's nothing else she should send, and after a week or two they may start calling applicants.
"""


test_data3 = """
#Person1#: I've heard that you provide very good service, so when I need a mover, I call you guys first.\n#Person2#: Thanks a lot for calling us. Could you tell me more about what you need us to do?\n#Person1#: Oh, you see, we are on the 8th floor, and moving into the 6th floor in another building. It is about 15 kilometers to get there.\n#Person2#: OK, the cost depends on the floor to move to, the distance between two places and the amount of the furniture to move.\n#Person1#: How much will it cost in that case?\n#Person2#: Oh, let me see. It fits the second standard rates. Have a look at the contract, please.\n#Person1#: Your charge is divided into two parts, the Payment in Advance and the rest. I thought that I should pay all of it before moving.\n#Person2#: No, firstly we sign the contract ; you pay 50 % of what it costs, and the rest when we finish moving.\n#Person1#: The damage and compensation item confuses me. Could you give some explanation?\n#Person2#: OK. If any of the articles was damaged during moving, you may make a claim for compensation with our department.
"""

test_data3b = """
I've heard that you provide very good service, so when I need a mover, I call you guys first. Thanks a lot for calling us. Could you tell me more about what you need us to do? Oh, you see, we are on the 8th floor, and moving into the 6th floor in another building. It is about 15 kilometers to get there. OK, the cost depends on the floor to move to, the distance between two places and the amount of the furniture to move. How much will it cost in that case? Oh, let me see. It fits the second standard rates. Have a look at the contract, please. Your charge is divided into two parts, the Payment in Advance and the rest. I thought that I should pay all of it before moving. No, firstly we sign the contract ; you pay 50 % of what it costs, and the rest when we finish moving. The damage and compensation item confuses me. Could you give some explanation? OK. If any of the articles was damaged during moving, you may make a claim for compensation with our department.
"""

test_data3_summary = """
#Person1# calls #Person2# because #Person1# needs a mover. #Person1# tells #Person2# what needs them to do and asks for the cost. #Person2# shows the contract and explains the cost and compensation.
"""

test_data4 = """
Hello. Can I help you? Yes, I hope so. I would like to register for Comp Lit 287. I'm sorry, but that class is already full. And also, students are supposed to register through the touch-tone registration system. I know. I already tried to register for it by phone, but the computer won't let me. That's because it's full. But I'm a new student here. I thought maybe there was some way I could get into the class. I thought I should come and talk to you in the department office. Well, I could put you on a waiting list. But that doesn't guarantee you will get into the class. What is your name? My name is Karen Huang. That's spelled H - U - A - N - G. Alright. And what is your major? I'm a comparative literature major. Wait a minute. You're a Comp Lit major? Yes, that's right. Why didn't you tell me? I didn't know you were one of our students. That's why I'm trying to get into Comp Lit 287. I know it's a required class. And Professor Cohen told me I need to take it. The university computer system saves extra places, in class 287 for comp lit students. I can give you a special code. When you register by phone, you can use the code to get into the class. Even if the class is full? That's right. Oh, I didn't know that. Sure. Here is the code number, with information on how to use it. Thank you. So you think I will be able to get in with this? Sure. Just call the touch-tone registration system again. Then, follow the directions on the sheet. You will get in no problem. Thanks. Next time you come in here, I will recognize you.
"""

test_data5 = """
IBA, Client Services Department. Shelley speaking, how can I help? Client Services? Oh, hello. I need your help. Certainly, that's what we're here for. What can I help you with? I'm a tourist in this city and unfortunately I've lost my card! Calm down, Sir. Is that an IBA Debit or Credit Card? Credit Card. The International Credit Card, I can't find it anywhere. Just calm down, Sir. OK, when do you think you lost it? I'm not 100 % sure, around an hour ago I guess. I had it in the hotel lobby bar ; I used it to charge something to my room. I obviously didn't pick it up again. That's fine, Sir. Let me just take some details FRCM you and we can help you. Thank you. Thank you very much.
"""