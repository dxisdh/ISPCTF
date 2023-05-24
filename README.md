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
| [Hash Number](#Hash-Number) | Crypto | `ISPCTF{That_iS_Special_Number}` |
| [Pointer 2](#Pointer-2) | RE | `ISP{302753d5b52596eb75b89c11cc30e5c7}`|
| [Basic Rev] | RE | `ispctf{St4RbuCk5_c0ffee}`|
| [Pointer 1] | RE | `flag{5h1n1n'_5t4r5_ju5t_l1k3_ur_sm1l3}`|
| [Basic For](#Basic-For) | Forensics | `ISPCTF{H4i_d3p_tr41_v0_c0_10}`|
| [New Chunk](#New-Chunk) | Forensics | `ISPCTF{Thank_to_fix_this_file}`|
| [Metadata is so good](#Metadata-is-so-good) | Forensics | `ISPCTF{137_ch3ck_m3tadata}`|
| [What is File Format?](#What-is-File-Format) | Forensics | `ISPCTF{0n3_f0r_a11_d3kn}`|
| [QR](#QR) | Forensics | `ISPCTF{h4i_d3p_z4i_y34h_y34h}`|
| [Catch Me](#Catch-Me) | Forensics | `ISPCTF{c4tch_m3}`|
| [Gờ rép](#Gờ-rép) | Forensics | `ISPCTF{G00d_luck_N3xt_Y34r}`|
| [Good, nice, excellent](#Good-nice-excellent) | Forensics | `ISPCTF{y0u_kn0vv_m0r3_t0o1}`|
| [Malware](#Malware) | Forensics | `ISPCTF{trojan.midie/cometer}`|
| [Information PCAP](#Information-PCAP) | Forensics | `ISPCTF{Rice_as_one}`|
| [Không chỉ là giao thức](#Không-chỉ-là-giao-thức) | Forensics | `ISPCTF{Ch3cK_Pr0toco1}`|
| [Beautiful day to drive :>](#Beautiful-day-to-drive) | OSINT | `ISPCTF{MEANDERING_WAY}`|
| [Find me before they do!](#Find-me-before-they-do) | OSINT | `ISPCTF{860-232-8886}`|
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

# Hash Number
Con số yêu thích của bạn là gì?

Form Flag: ISPCTF{}

[favorite_num.py](https://github.com/dxisdh/ISPCTF/tree/main/File%20chall/Hash%20Number)
#### Solution
Mở source code lên, ta thấy ở hàm main() có cho biết chiều dài của số cần tìm là 8 chữ số. Ta viết lại hàm main như sau:
```
def main():
    for i in range (10000000,99999999):
         if check_input(str(i)) == 1:
             print(str(i))
```
Ở đây ta sẽ viết một vòng lặp chạy từ 10000000 cho đến 99999999, sau đó kiểm tra xem trong khoảng đó nếu có số nào trả về kết quả 1 thì in ra số đó
Chương trình sẽ trả lại cho ta con số cần tìm. Khôi phục lại code ban đầu, chạy lại chương trình, nhập số vừa tìm được và nhận flag

Flag: `ISPCTF{That_iS_Special_Number}`

# Pointer 2

[pointer2.c](https://github.com/dxisdh/ISPCTF/tree/main/File%20chall/Pointer%202)
#### Solution
Mở source code lên, ta sẽ phân tích hàm fuzz trước. 
```
int fuzz(char *key) {
    char char1[10], char2[10], char3[10], char4[10];
    memset(char1, 0, 10);
    memset(char2, 0, 10);
    memset(char3, 0, 10);
    memset(char4, 0, 10);

    strncpy(char1, key, 8);
    strncpy(char2, key + 8, 8);
    strncpy(char3, key + 16, 8);
    strncpy(char4, key + 24, 8);

    memset(key, 0, 32);

    strcat(key, char3);
    strcat(key, char1);
    strcat(key, char4);
    strcat(key, char2);

    return 1;
}
```
Hàm fuzz sẽ nhận kí tự key làm đầu vào và sẽ trả lại một số nguyên. Ta sẽ khởi tạo 4 mảng kí tự char1, char2, char3, char4 gồm 10 phần tử và tất cả các phần tử đều được đặt bằng 0 nhờ hàm memset. Sau đó, hàm strncpy sẽ sao chép 8 kí tự đầu tiên vào char1, 8 kí tự tiếp theo vào char2, 8 kí tự sau vào char3 và 8 kí tự cuối cùng vào char4. Sau đó hàm memset sẽ lại đặt 32 kí tự trong key bằng 0. Tiếp đó, hàm strcat sẽ nối key với char3, char1, char4 và char2. Cuối cùng hàm sẽ trả về giá trị 1 sau khi thực hiện các dòng lệnh phía trên.

Tiếp theo ta sẽ đi vào hàm main().
```
int main(int argc, char **argv) {
    printf("Let's see if you passed the right flag...\n");
    if (argc == 2)
        if (strlen(*(argv + 1)) == 32)
            if (!fuzz(*(argv + 1)))
                printf("Wrong Direction.");
            else if (!strncmp(*(argv + 1), "302753d5b52596eb75b8", 0x14))
                if (!strncmp(*(argv + 1) + 20, "9c11cc30e5c7", 12))
                    printf("True.");
                else
                    printf("Try again.");
            else
                printf("Try again.");
        else
            printf("Try again.");
    else
        printf("Try again.");
}
```
Hàm main() sẽ thực hiện một loạt các câu lệnh if - else để kiểm tra các điều kiện. Đầu tiên chương trình sẽ kiểm tra số lượng tham số ta truyền vào có bằng 2 hay không, nếu không thì sẽ in ra "Try again". Tiếp đó chương trình sẽ kiểm tra xem chiều dài của giá trị mà con trỏ của tham số dòng lệnh đầu tiên chứa có bằng 32 không, nếu không thì sẽ in ra "Try again", từ đó ta biết được flag có chiều dài bằng 32. Chương trình sẽ tiếp tục kiểm tra giá trị mà hàm fuzz với giá trị nhập vào là giá trị mà con trỏ của tham số dòng lệnh đầu tiên chứa trả lại có khác giá trị 1 hay không, nếu có thì sẽ in ra "Wrong Direction" và nếu không thì in ra "Try again". Ta sẽ phân tích câu lệnh if cuối cùng:
```
else if (!strncmp(*(argv + 1), "302753d5b52596eb75b8", 0x14))
     if (!strncmp(*(argv + 1) + 20, "9c11cc30e5c7", 12))
         printf("True.");
     else
         printf("Try again.");
```
Ta thấy 0x14 là 1 số được biểu diễn dưới dạng hệ thập lục phân và là số 20 trong hệ thập phân. Hàm strncmp sẽ so sánh xem 20 kí tự đầu tiên của giá trị mà con trỏ của tham số dòng lệnh đầu tiên chứa có bằng với xâu 302753d5b52596eb75b8 hay không, nếu có sẽ so sánh tiếp 12 kí tự tiếp theo của giá trị mà con trỏ của tham số dòng lệnh đầu tiên chứa và đã thêm 20 kí tự trên có bằng với xâu 9c11cc30e5c7 hay không, nếu đúng sẽ in ra "True." còn nếu sai sẽ in ra "Try again.". Từ đó ta biết flag cần tìm là `302753d5b52596eb75b89c11cc30e5c7`.

Flag: `ISP{302753d5b52596eb75b89c11cc30e5c7}`
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

# QR

Một nửa còn lại của mã QR đang ở đâu???

[haidz.png](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/QR/haidz.png)
#### Solution
Dựa trên đề bài, ta xem thử kích thước của ảnh bằng cách xem Properties

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/QR/QR_4.png>
Ta có thể thấy chiều dài của ảnh là 2100 pixels còn chiều cao của ảnh là 1000 pixels. Ta sẽ sửa 4 bit chiều cao của ảnh bằng cách sử dụng HxD. Ta đổi 2000 sang hệ 16 được 07D0. Sau đó thay 4 bit chiều cao của ảnh trong IHDR chunk: `00 00 03 E8` -> `00 00 07 D0`

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/QR/QR_1.png>
Lưu lại và ta có mã QR đầy đủ

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/QR/QR.png>
Sử dụng web đọc QR ta được 1 đường link

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/QR/QR_2.png>
Mở link đó và ta nhận được flag

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/QR/QR_3.png>

Flag: `ISPCTF{h4i_d3p_z4i_y34h_y34h}`

# Catch Me

Form Flag: ISPCTF{}

[catch_me.pcapng](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Catch%20Me/catch_me.pcapng)
#### Solution
Ta nhận được một file có đuôi .pcapng. Ta sẽ sử dụng Wireshark để phân tích. Mở Wireshark lên, ta sẽ thử phân tích protocol TCP. Chọn Analyze -> Follow -> TCP Stream

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Catch%20Me/catchme_1.png>
Ta nhận được flag:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Catch%20Me/catchme_2.png>

Flag: `ISPCTF{c4tch_m3}`

# Gờ rép

[SVNQe04wdF9hX1IzQWxfRmxBZ30.txt](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/G%E1%BB%9D%20r%C3%A9p/SVNQe04wdF9hX1IzQWxfRmxBZ30.txt)
#### Solution
Ta nhận được một file .txt. Dựa vào đề bài, ta sẽ sử dụng grep để tìm các mảnh ghép của flag (ở đây mình đổi tên file sang text.txt). Đầu tiên ta sẽ tìm mảnh ghép đầu tiên bằng cách nhập: `grep 'ISPCTF' text.txt`. Ta được mảnh ghép đầu tiên:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/G%E1%BB%9D%20r%C3%A9p/grep_1.png>
Ta đoán phía sau sẽ cần dấu `_` nên ta sẽ nhập với cú pháp tương tự, chỉ cần thay `ISPCTF` sang `_`. Ta tìm được hai mảnh ghép tiếp theo:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/G%E1%BB%9D%20r%C3%A9p/grep_2.png>
<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/G%E1%BB%9D%20r%C3%A9p/grep_3.png>
Sau khi nhìn mảnh ghép thứ 3 thì ta đoán còn 1 mảnh ghép cuối cùng. Thế nên ta sẽ cần dấu } để kết thúc. Làm tương tự như trên, ta được mảnh ghép cuối cùng:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/G%E1%BB%9D%20r%C3%A9p/grep_4.png>
Ghép tất cả các mảnh ghép lại ta được flag hoàn chỉnh.

Flag: `ISPCTF{G00d_luck_N3xt_Y34r}`

# Good, nice, excellent

[Noice.zip](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Noice/Noice.zip)
#### Solution
Ta nhận được 1 file zip trong đó có chứa một file ảnh và một file text. Mở thử file text ra, ta thấy bên trong có dãy số nhị phân bên cạnh các kí tự

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Noice/noice_1.png>
Ta thấy tên file có điều gì đó đặc biệt. Nếu ta thử đổi 12 ra số nhị phân ta sẽ nhận được 1100. Thử tìm 1100 trong file text, ta sẽ ghép được các kí tự vào với nhau và cuối cùng nhận được: `Stegosuite`. Ta sẽ dùng Stegosuite để phân tích ảnh và nhận được flag.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Noice/noice_2.png>

Flag: `ISPCTF{y0u_kn0vv_m0r3_t0o1}`

# Malware

AI hiện có thể bị nhiễm phần mềm độc hại! Sau khi hỏi ChatGPT về công thức nấu súp cà chua, công thức nấu ăn main_background.png đã được cung cấp. Sau khi chạy các lệnh md5sum recipe.png > result.txt và cat result.txt, kết quả đầu ra sau đây được nhận: 737bc4c1e193d54abcbac2bac6ff89fe10bb3f31

ISPCTF{Popular threat label}

Gợi ý: Sản phẩm chống virus. Công cụ quét trang web.
#### Solution
Dựa vào gợi ý, ta sẽ tra thử website chuyên quét và diệt virus trên mạng và tìm được trang web VirusTotal. Nhập phần kết quả kia vào mục Search, ta sẽ tìm được flag.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Malware/malware_1.png>

Flag: `ISPCTF{trojan.midie/cometer}`

# Information PCAP

[lmaolmao.pcapng](https://github.com/dxisdh/ISPCTF/tree/main/File%20chall/Information%20PCAP)
#### Solution
Ta nhận được một file pcapng. Ta sẽ thử phân tích file này bằng Wireshark. Mở Wireshark lên, ta sẽ thử phân tích protocol TCP. Chọn Analyze -> Follow -> TCP Stream.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Information%20PCAP/infor_1.png>
Ta nhận thấy dấu hiệu của file JPEG dựa vào định dạng JFIF sau khi follow TCP. Cho nên ta đoán rằng file đã bị chỉnh sửa định dạng. Chuyển Show data as ASCII -> Show data as Raw để lấy mã hex.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Information%20PCAP/infor_2.png>
Mở file pcapng bằng HxD để thay thế mã hex hiện tại bằng mã hex mới (bỏ 4 dòng đầu tiên)

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Information%20PCAP/infor_3.png>
Lưu lại và đổi đuôi file sang jpeg và ta nhận được một bức ảnh:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Information%20PCAP/lmaolmao.jpeg>
Ta thấy rằng flag đã bị giấu kín. Ta sẽ sử dụng futureboys để phân tích:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Information%20PCAP/infor_4.png>
Nhấn Submit và ta sẽ nhận được flag:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Information%20PCAP/infor_5.png>

Flag: `ISPCTF{Rice_as_one}`

# Không chỉ là giao thức

[file.pcapng](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Kh%C3%B4ng%20ch%E1%BB%89%20l%C3%A0%20giao%20th%E1%BB%A9c/file.pcapng)
#### Solution
Ta nhận được một file pcapng. Ta sẽ thử phân tích file này bằng Wireshark. Mở Wireshark lên, ta sẽ thử phân tích protocol TCP. Chọn Analyze -> Follow -> TCP Stream. Sau đó ta sẽ tìm điều khả nghi dựa vào các dòng Stream và tìm được tại Stream 9.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Kh%C3%B4ng%20ch%E1%BB%89%20l%C3%A0%20giao%20th%E1%BB%A9c/not_protocol_1.png>

Ta nhận thấy dấu hiệu của file JPEG dựa vào định dạng JFIF sau khi follow TCP. Cho nên ta đoán rằng file đã bị chỉnh sửa định dạng. Chuyển Show data as ASCII -> Show data as Raw để lấy mã hex.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Kh%C3%B4ng%20ch%E1%BB%89%20l%C3%A0%20giao%20th%E1%BB%A9c/not_protocol_2.png>

Mở file pcapng bằng HxD để thay thế mã hex hiện tại bằng mã hex mới (bỏ dòng đầu tiên)

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Kh%C3%B4ng%20ch%E1%BB%89%20l%C3%A0%20giao%20th%E1%BB%A9c/not_protocol_3.png>

Lưu lại và đổi đuôi file sang jpeg và ta nhận được flag.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Kh%C3%B4ng%20ch%E1%BB%89%20l%C3%A0%20giao%20th%E1%BB%A9c/file.jpeg>

Flag: `ISPCTF{Ch3cK_Pr0toco1}`

# Beautiful day to drive :>

Hôm nay là một ngày đẹp trời để lái xe hóng gió, liệu các thám tử tài ba có thể chỉ ra con đường mà tôi đang đi không ? Ví dụ: Tôi đang ở đường Trần Phú thì form flag sẽ là: ISPCTF{TRAN_PHU}

Hint: Tôi đang ở đâu đó ở bang Texas, Mỹ

[IMG_1485.MOV](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Beautiful%20day%20to%20drive/IMG_1485.MOV)
#### Solution
Ta nhận được 1 video về một cảnh quay. Nếu chạy bằng phần mềm chạy video thì ta chỉ thấy một phần của tên đường:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Beautiful%20day%20to%20drive/beautiful_1.png>
Cho nên ta sẽ sử dụng exiftool để tìm thông tin về đoạn video. Ta nhập `exiftool IMG_1485.MOV` vào cửa sổ lệnh. Và ta tìm được định vị của đoạn video là: `32°58'51.2"N 96°46'43.0"W`

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Beautiful%20day%20to%20drive/beautiful_2.png>
Mở Google Maps và nhập định vị trên, ta tìm được tên đường, cũng chính là flag:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Beautiful%20day%20to%20drive/beautiful_3.png>

Flag: `ISPCTF{MEANDERING_WAY}`

# Find me before they do!

I'm a hacker on the run from the cops. But my friend, I'll leave some clues for you to find me. Note this carefully: I usually eat sushi in a restaurant with a nearby view that looks like this. After that, I often go to the park and sit by the nearby lake, which may be called Batterson. If you find out where the restaurant is, please contact the sushi restaurant. Just tell the restaurant owner their phone number, and I'll know it's you who called. Then wait for my next instruction! If you don't hear anything from me, I may have been caught!

Flag form: ISPCTF{}

[340494030_242932678297283_41190817524115878_n.jpg](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Find%20me%20before%20they%20do/340494030_242932678297283_41190817524115878_n.jpg)
#### Solution
Ta nhận được một bức ảnh. Ta sẽ dựa vào tòa nhà có chữ CHASE để xem nó là gì. Sử dụng Google Lens để tìm kiếm, ta biết được tòa nhà đó là Chase Bank.

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Find%20me%20before%20they%20do/findme_5.png>
Tuy nhiên lại có rất nhiều chi nhánh của ngân hàng Chase, thế nên ta sẽ thu hẹp phạm vi tìm kiếm bằng cách dựa vào câu sau: `After that, I often go to the park and sit by the nearby lake, which may be called Batterson.` (Sau đó, tôi thường đến công viên và ngồi bên cạnh một cái hồ, tên của công viên đó chắc là Batterson). Điều đó cho biết rằng ta chỉ cần tìm các chi nhánh ngân hàng Chase gần công viên Batterson, sau đó xem chi nhánh nào có bức ảnh gần giống với bức ảnh ta có. Thì trong số đó có chi nhánh tại đường West Hartford là giống nhất:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Find%20me%20before%20they%20do/findme_1.png>
Mà tác giả đã nói rằng mình hay ăn sushi ở một nhà hàng, thế nên ta thấy ngay bên cạnh ngân hàng đó ta có một nhà hàng sushi tên là ICHIRO HIBACHI & SUSHI:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Find%20me%20before%20they%20do/findme_2.png>
Sau khi tìm được nhà hàng đó, tiếp theo ta cần tìm tên chủ nhà hàng. Tra google cụm `Ichiro Hibachi & Sushi owner`, ta tìm được 1 trang web có tổng hợp thông tin về nhà hàng này và ta tìm được tên chủ là Andy Pan:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Find%20me%20before%20they%20do/findme_3.png>
Đề bài yêu cầu tìm số điện thoại của chủ nhà hàng, nên ta lại tra google cụm `Andy Pan Ichiro Hibachi & Sushi`, ta tìm được 1 trang web có tổng hợp những người tên là Andy Pan. Sử dụng tổ hợp Ctrl + F và ghi owner để loại trừ dần và ta tìm được 2 số:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Find%20me%20before%20they%20do/findme_4.png>
Thế nhưng nếu truy cập vào trang web của nhà hàng thì ta sẽ thấy số đầu tiên là của nhà hàng, chứ không phải của chủ nhà hàng. Cho nên số điện thoại còn lại chính là số điện thoại của chủ cửa hàng:

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/Find%20me%20before%20they%20do/findme_6.png>
Sửa lại số điện thoại theo format: XXX-XXX-XXXX và ta thu được flag.

Flag: `ISPCTF{860-232-8886}`
