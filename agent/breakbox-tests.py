from breakbox import to_shell_command
import unittest


class TestCommandBuilders(unittest.TestCase):
	
	def test_isolate_webserver(self):
		params={ 
			'name': 'isolate-web-server',
			'type': 'NETWORK_FAILURE',
			'direction': 'IN',
			'from': 'ALL',
			'to_port': 80,
			'protocol': 'TCP'
		}
		self.assertEqual(to_shell_command('add', params), 'iptables -A INPUT -p TCP -j DROP --dport 80')


	def test_isolate_webserver_delete(self):
		params={
      		'name': "isolate-web-server",
      		'type': "NETWORK_FAILURE",
      		'direction': "IN",
      		'from': "ALL",
      		'to_port': 81,
      		'protocol': "TCP"
      	}
		self.assertEqual(to_shell_command('delete', params), 'iptables -D INPUT -p TCP -j DROP --dport 81')
		
	def test_isolate_udp_server(self):
		params={
      		'name': "isolate-streaming-server",
      		'type': "NETWORK_FAILURE",
      		'direction': "IN",
      		'from': "ALL",
      		'to_port': 8111,
      		'protocol': "UDP"
      	}
		self.assertEqual(to_shell_command('add', params), 'iptables -A INPUT -p UDP -j DROP --dport 8111')
		
	def test_webserver_shut_down(self):
		params={
      		'name': "web-server-down",
      		'type': "SERVICE_FAILURE",
      		'direction': "IN",
      		'from': "ALL",
      		'to_port': 8080,
      		'protocol': "TCP"
      	}
		self.assertEqual(to_shell_command('add', params), 'iptables -A INPUT -p TCP -j REJECT --dport 8080')
		
	def test_client_dependency_unreachable(self):
		params={
      		'name': "connectivity-to-dependency-down",
      		'type': "NETWORK_FAILURE",
      		'direction': "OUT",
			'to': 'my.dest.host.com',
      		'to_port': 443,
      		'protocol': "TCP"
      	}
		self.assertEqual(to_shell_command('add', params), 'iptables -A OUTPUT -p TCP -j DROP --dport 443 -d my.dest.host.com')



if __name__ == '__main__':
    unittest.main()