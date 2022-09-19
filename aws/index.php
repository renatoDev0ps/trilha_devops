<?php
  $mac = "http://169.254.169.254/latest/meta-data/network/interfaces/macs/";
  $mac1 = file_get_contents($mac);
  $url = "http://169.254.169.254/latest/meta-data/network/interfaces/macs/$mac1/public-ipv4s";
  $instance_id = file_get_contents($url)
  echo "<h1><br/><br/><p align='center'><font color='#adff2f' size='350'> instance ID: <font color='red'>" . $instance_id . "</p>,br/></font></font></h1>"
?>