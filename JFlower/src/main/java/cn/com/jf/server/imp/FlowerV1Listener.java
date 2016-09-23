package cn.com.jf.server.imp;

import java.util.List;

import javax.transaction.Transactional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import cn.com.jf.bean.UserInfo;
import cn.com.jf.dao.UserInfoMapper;
import cn.com.jf.server.FlowerV1Interface;

@Service
@Transactional
public class FlowerV1Listener implements FlowerV1Interface{

	
	@Autowired
	private UserInfoMapper userMapper;
	
	/* (non-Javadoc)
	 * @see cn.com.jf.server.FlowerV1Interface#getAllUser()
	 */
	@Override
	public List<UserInfo> getAllUser() {
		// TODO Auto-generated method stub
		return userMapper.findAll();
	}
	
}