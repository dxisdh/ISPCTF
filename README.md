# ISPCTF
Writeup các bài đã solve trên web CTF của CLB ISP
| Title | Category | Flag | 
| :----- | :---------- | :-------------- | 
| [Rail_fence](#Rail-fence) | Crypto | `ISPCTF{That_Is_Rail_Fence_Cipher}`|
| [Base 64](#Base-64) | Crypto | `ISPCTF{B4s3_S4u_4}`|
| [ROT_ROT](#ROT-ROT) | Crypto | `ISPCTF{R0T_1S_4M4Z1N9!!!}`|
| [TOR74](#TOR74) | Crypto | `ISPCTF{N0w_u_kN0W_how_2_use_R47}`|
| [rsa_1](#rsa-1) | Crypto | `ISPCTF{welcome_to_rsa}`|
| [Xor Cipher] | Crypto | `ISPCTF{X0r_C1ph3r_1s_s0_S1mpl3}`|
| [rsa_3](#rsa-3) | Crypto | `ISPCTF{e=1_any_thing_not_change}`|
| [rsa_2](#rsa-2) | Crypto | `ISPCTF{Now_you_know_factor_N}`|
| [Pointer 2] | RE | `ISP{302753d5b52596eb75b89c11cc30e5c7}`|
| [Basic Rev] | RE | `ispctf{St4RbuCk5_c0ffee}`|
| [Basic For](#Basic-For) | Forensics | `ISPCTF{H4i_d3p_tr41_v0_c0_10}`|
| [New Chunk](#New-Chunk) | Forensics | `ISPCTF{Thank_to_fix_this_file}`|
| [Metadata is so good](#Metadata-is-so-good) | Forensics | `ISPCTF{137_ch3ck_m3tadata}`|
| [What is File Format?](#What-is-File-Format) | Forensics | `ISPCTF{0n3_f0r_a11_d3kn}`|
| [QR] | Forensics | `ISPCTF{h4i_d3p_z4i_y34h_y34h}`|
| [Catch Me] | Forensics | `ISPCTF{c4tch_m3}`|
| [Gờ rép] | Forensics | `ISPCTF{G00d_luck_N3xt_Y34r}`|
| [Beautiful day to drive] | OSINT | `ISPCTF{MEANDERING_WAY}`|
| [Find me before they do!] | OSINT | `ISPCTF{860-232-8886}`|
| [Find me before they do! (2)] | OSINT | `ISPCTF{70_FOUR_MILE_RD}`|
| [Conversation] | General | `ISPCTF{here_is_random_messageBruhh}`|

# Rail_fence
Bạn có thể giải mã nó không?

[Encrypted.txt](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Rail_fence/Encrypt.txt)
#### Solution
Mở file text lên ta nhận được một đoạn mã

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Rail_fence/rail_fence_3.png>
Dựa vào đề bài, ta tìm tool decode Rail Fence, tích vào ô KEEP PUNCTUATION AND SPACES, sau đó chọn AUTOMATIC DECRYPTION để tool decrypt tất cả các trường hợp có thể xảy ra

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Rail_fence/rail_fence_1.png>
Ta thấy dòng thứ 3 hiện ra flag cần tìm: 

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Rail_fence/rail_fence_2.png>
Flag: `ISPCTF{That_Is_Rail_Fence_Cipher}`

# Base 64
Base64 xxx

[base64.txt](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Base%2064/base64.txt)
#### Solution
Mở file text lên ta nhận được một đoạn mã

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Base%2064/base64_1.png>
Dựa vào đề bài, ta tìm tool decode Base 64 và bắt đầu decrypt

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Base%2064/base64_2.png>
Nhận thấy tool decrypt ra một đoạn mã Base 64 khác, tiếp tục decrypt cho đến khi nhận được flag

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Base%2064/base64_3.png>
Flag: `ISPCTF{B4s3_S4u_4}`

# ROT_ROT

[ROT.txt](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/ROT_ROT/ROT.txt)
#### Solution
Mở file text lên ta nhận được một đoạn mã

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/ROT_ROT/rot_rot_1.png>
Dựa vào đề bài, ta đoán phải sử dụng tool ROT Cipher 2 lần. 

Sử dụng tool ROT Cipher lần 1 ta tìm được một đoạn mã khả nghi: VFCPGS{E0G_1F_4Z4M1A9!!!}

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/ROT_ROT/rot_rot_2.png>

Tiếp tục ROT lần 2 ta tìm được flag

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/ROT_ROT/rot_rot_3.png>
Flag: `ISPCTF{R0T_1S_4M4Z1N9!!!}`

# TOR74

Try to hit this target:

[TOR74.txt](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/TOR74/TOR74.txt)
#### Solution
Mở file text lên ta nhận được một đoạn mã

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/TOR74/tor74_1.png>
Dựa vào đề bài, ta tìm tool ROT-47 Cipher và thu được flag

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/TOR74/tor74_2.png>
Flag: `ISPCTF{N0w_u_kN0W_how_2_use_R47}`

# rsa_1

>nc 157.245.150.103 7779
#### Solution
Ta kết nối netcat và nhận được 3 giá trị p, q và e

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_1/rsa1_1.png>
Ta sẽ viết chương trình Python để tìm key

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_1/rsa1_2.png>
Ta nhận được key

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_1/rsa1_3.png>
Nhập key ta tìm được flag

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_1/rsa1_4.png>
Flag: `ISPCTF{welcome_to_rsa}`

# rsa_3

[cipher](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_3/cipher)
[rsa_3.py](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_3/rsa_3.py)
#### Solution
Tải source code về, ta thấy trong hàm encrypt thực hiện chuyển từng kí tự trong flag ở hàm init thành mã ASCII, sau đó nâng lên lũy thừa 1 mod n trong hàm init. Sau đó chuyển sang 1 xâu byte có độ dài là 5 và lưu vào một list tên là cipher. List đó sẽ được viết vào file cipher, kết thúc một kí tự sẽ xuống dòng 1 lần. Hàm decrypt đọc file cipher sau đó tách từng kí tự thành từng xâu byte và chuyển từng xâu byte đó sang dạng số nguyên và decrypt bằng key riêng. Nhưng vì e = 1 nên các kí tự trong file cipher không bị biến đổi. Ta mở file cipher bằng Notepad, thu được flag

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_3/rsa3_1.png>
Flag: `ISPCTF{e=1_any_thing_not_change}`

# rsa_2

[cipher.txt](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_2/cipher.txt)
[rsa_2.py](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_2/rsa_2.py)
#### Solution
Mở source code lên, ta có 2 giá trị n và e. Ta thấy trong hàm rsa thực hiện mã hóa từng kí tự trong flag thành số với phép toán lấy mod n của mess^-e. Nên đầu tiên ta sẽ phân tích n thành 2 thừa số nguyên tố p và q để tìm key d:
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_2/rsa2_1.png>

Làm tương tự bài rsa_1, ta tìm được key d:
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_1/rsa1_3.png>

Áp dụng công thức giải mã: m = pow(c, d, n) với c là cipher.

Ta có chương trình Python như sau với c là từng dòng trong file cipher.txt:
```
    d = 121832886702415731577073962957377780195510499965398469843281
    c = 601748807654457784008912152319168422704193274988376714148917 // dòng đầu tiên trong file cipher.txt
    n = 882564595536224140639625987659416029426239230804614613279163
    m = pow(c, d, n)
    print(m)
```
Sau khi chạy chương trình ta thu được 1 số là 73, tương đương với I trong bảng mã ASCII. Tương tự với các dòng sau, ta thu được 1 dãy số hoàn chỉnh như sau:
> 73 83 80 67 84 70 123 78 111 119 95 121 111 117 95 107 110 111 119 95 102 97 99 116 111 114 95 78 125

Dùng tool chuyển đổi hệ thập phân sang bảng mã ASCII, ta thu được flag:
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/rsa_2/rsa2_2.png>
Flag: `ISPCTF{Now_you_know_factor_N}`

# Basic For

[haianh.jpg](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Basic%20For/haianh.jpg)
#### Solution
Ta nhận được một bức ảnh. Mở ảnh bằng Notepad, không thấy điều gì đặc biệt xuất hiện. Ta lập tức nghĩ ngay đến HxD. Mở HxD lên và ta nhìn thấy một đoạn mã Base 64: `SVNQQ1RGe0g0aV9kM3BfdHI0MV92MF9jMF8xMH0=`
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Basic%20For/basicfor_1.png>

Dùng tool decode Base 64, ta nhận được flag:
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Basic%20For/basicfor_2.png>
Flag: `ISPCTF{H4i_d3p_tr41_v0_c0_10}`

# New Chunk

[Avatar](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/New%20Chunk/Avatar)
#### Solution
Ta nhận được một file. Mở file bằng Notepad, ta thấy dòng đầu về định dạng ảnh có vẻ là PNG nhưng đã bị thay đổi. Mở HxD lên để sửa lại đoạn chunk và lưu lại.
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/New%20Chunk/newchunk_1.png>

Sau khi sửa xong, ta thêm định dạng ảnh .png vào đằng sau tên file và thu được flag:
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/New%20Chunk/newchunk_2.png>
Flag: `ISPCTF{Thank_to_fix_this_file}`

# Metadata is so good

[rice.jpg](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Metadata%20is%20so%20good/rice.jpg)
#### Solution
Ta nhận được một bức ảnh. Mở ảnh bằng Notepad và ta tìm thấy flag:
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Metadata%20is%20so%20good/metadata_1.png>
Flag: `ISPCTF{137_ch3ck_m3tadata}`

# What is File Format?

[mizuku](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/What%20is%20File%20Format/mizuku)
#### Solution
Ta nhận được một file. Mở file bằng Notepad, ta thấy định dạng JFIF, nên ta có thể đoán đây là định dạng ảnh JPEG nhưng đã bị thay đổi.
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/What%20is%20File%20Format/whatisfileformat_1.png>

Mở HxD lên để sửa lại đoạn chunk chứa định dạng ảnh: `37 48 26 93 19 10` -> `FF D8 FF E0 00 10` và lưu lại.
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/What%20is%20File%20Format/whatisfileformat_2.png>

Sau khi sửa xong, ta thêm định dạng ảnh .jpeg vào đằng sau tên file và thu được flag:
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/What%20is%20File%20Format/mizuku.jpeg>
Flag: `ISPCTF{0n3_f0r_a11_d3kn}`
