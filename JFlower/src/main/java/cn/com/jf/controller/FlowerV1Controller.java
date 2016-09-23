package cn.com.jf.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import cn.com.jf.bean.UserInfo;
import cn.com.jf.server.FlowerV1Interface;

/** @author zhangyh2
 * FlowerV1Controller
 * 下午2:30:59
 * TODO 测试的第一个版本的第一个接口列表
 */
@Service
@RequestMapping("/v1/api")
public class FlowerV1Controller{
	
	@Autowired
	private FlowerV1Interface ser;
	
	@RequestMapping(value = "/te")
	@ResponseBody
	public List<UserInfo> findUser(){
		System.out.println("FlowerV1Controller  findUser");
		return ser.getAllUser();
	}
}