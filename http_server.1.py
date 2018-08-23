#!/usr/bin/env Python
# -*- coding:utf-8 -*-
# http_server.1.py 删除多余注释版本，带函数示例


import socket

HOST = ''  # localhost:本机，ip值，空：任意主机都可以访问
PORT = 8888
ADDR = (HOST, PORT)
BUFSIZE = 1024


def build_response(req_path):
    """构造服务器响应，注意HTTP协议的换行，以及不要多余空格"""
    response = f"""HTTP/1.1 200 OK

        <h1>hello {req_path}</h1>
        <img src="http://h.hiphotos.baidu.com/image/h%3D300/sign=a9f37a64f11f4134ff37037e151d95c1/c995d143ad4bd1137c1d50b556afa40f4afb0560.jpg" width="319.11357340720224" height="212.65927977839337">
        """.encode()  # 编码到bytes
    return response


def json_response(req_path):
    """构造服务器响应，注意HTTP协议的换行，以及不要多余空格"""
    response = f"""HTTP/1.1 200 OK

        <h1>hello {req_path}</h1>
        {{ "name": "Brett", "address": "北京路23号", "email": "123456@qq.com" }}
        """.encode('gbk')  # 编码到bytes ，f格式化内，json格式需要多一层{}
    return response


def jpg_response(req_path):
    """构造服务器响应，注意HTTP协议的换行，以及不要多余空格"""
    response = f"""HTTP/1.1 200 OK

        <h1>hello {req_path}</h1>
        <img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1534935879340&amp;di=4e7546dc93982c5cfa2ad675770eac14&amp;imgtype=0&amp;src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201603%2F19%2F20160319204738_ncLmd.jpeg" width="146" height="146" style="top: 48px; left: 611px; width: 246px; height: 246px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">
        """.encode()  # 编码到bytes
    return response


def jpg2_response(req_path):
    """构造服务器响应，注意HTTP协议的换行，以及不要多余空格"""
    response = f"""HTTP/1.1 200 OK

        <h1>hello {req_path}</h1>
        <img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1534935879340&amp;di=4e7546dc93982c5cfa2ad675770eac14&amp;imgtype=0&amp;src=http%3A%2F%2Fimg3.duitang.com%2Fuploads%2Fitem%2F201603%{req_path}" width="146" height="146" style="top: 48px; left: 611px; width: 246px; height: 246px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">
        """.encode()  # 编码到bytes
    return response


def wrong_response(req_path):
    """构造服务器响应，注意HTTP协议的换行，以及不要多余空格"""
    response = f"""HTTP/1.1 200 OK

        <h1>hello {req_path}</h1>
        <img class="currentImg" id="currentImg" onload="alog &amp;&amp; alog('speed.set', 'c_firstPageComplete', +new Date); alog.fire &amp;&amp; alog.fire('mark');" src="https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1534934812678&amp;di=0868f9f441b01d62ab312be2720d71c0&amp;imgtype=0&amp;src=http%3A%2F%2Fimg.zcool.cn%2Fcommunity%2F01a12555dee2546ac7251df897adfe.png%401280w_1l_2o_100sh.png" width="1280" height="573" style="top: 0px; left: 410px; width: 647.818px; height: 290px; cursor: pointer;" log-rightclick="p=5.102" title="点击查看源网页">
        """.encode()  # 编码到bytes
    return response


def start_server(sock):
    """使用socket开始HTTP服务
    """
    # 循环发送和接收数据
    while True:
        # 等待连接
        print('等待连接...')
        conn, addr = sock.accept()
        print('成功连接： ', addr)
        try:
            data = conn.recv(BUFSIZE)
            # print('收到数据：', data)   # 处理中文数据的显示
            if data:
                req_path = data.decode('utf-8').splitlines()[0] # 处理中文数据的显示,取到数值第一行
                print('收到数据第一行：', req_path)   
                method, path, http = req_path.split()
                print(f'切换URL地址到{path}')
                path_r = path[1:]
                if path_r == "image":
                    conn.sendall(build_response(path_r))  # 在这里处理数据
                elif path_r == "json":
                    conn.sendall(json_response(path_r))
                elif path_r == "pic/1.jpg":
                    path_j1 = path_r[4:]
                    conn.sendall(jpg_response(path_j1))
                elif path_r == "pic/2F20160319204738_ncLmd.jpeg":
                    path_j2 = path_r[4:]
                    conn.sendall(jpg2_response(path_j2))
                else:
                    conn.sendall(wrong_response(path_r))
        except Exception as e:
            print(e)
            break


def main():
    # 新建socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP相关参数

    # 绑定地址
    sock.bind(ADDR)

    # 监听连接的个数
    sock.listen(1)

    print('启动http服务')

    # 开始服务
    start_server(sock)

    # 关闭socket
    sock.close()


if __name__ == '__main__':
    main()