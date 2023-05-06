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
| [rsa_3] | Crypto | `ISPCTF{e=1_any_thing_not_change}`|
| [rsa_2] | Crypto | `ISPCTF{Now_you_know_factor_N}`|
| [Pointer 2] | RE | `ISP{302753d5b52596eb75b89c11cc30e5c7}`|
| [Basic For] | Forensics | `ISPCTF{H4i_d3p_tr41_v0_c0_10}`|
| [New Chunk] | Forensics | `ISPCTF{Thank_to_fix_this_file}`|
| [Metadata is so good] | Forensics | `ISPCTF{137_ch3ck_m3tadata}`|
| [What is File Format?] | Forensics | `ISPCTF{0n3_f0r_a11_d3kn}`|
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
Flag: ISPCTF{That_Is_Rail_Fence_Cipher}

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
Flag: ISPCTF{B4s3_S4u_4}

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
Flag: ISPCTF{R0T_1S_4M4Z1N9!!!}

# TOR74

Try to hit this target:

[TOR74.txt](https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/TOR74/TOR74.txt)
#### Solution
Mở file text lên ta nhận được một đoạn mã

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/TOR74/tor74_1.png>
Dựa vào đề bài, ta tìm tool ROT-47 Cipher và thu được flag

<img src= https://github.com/dxisdh/ISPCTF/blob/main/File%20chall/TOR74/tor74_2.png>
Flag: ISPCTF{N0w_u_kN0W_how_2_use_R47}

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
Flag: ISPCTF{welcome_to_rsa}
