vagrant fabric
====
vagrantをfabricでセットアップしてみる

## Description

| インストール | version |
|:-----------|:------------|
| php        |5.6.7|
| apache     |2.4.10|
| mysql      |5.5.41|
| python     |2.7.3|
| composer   |-|
| phpunit    |4.3|

## Requirement

以下をインストール(macのみでしか検証してません！！)

- virualbox
  - [Downloads – Oracle VM VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- vagrant
  - [Download Vagrant - Vagrant](https://www.vagrantup.com/downloads.html)
- fabric

```
$ easy_install pip
$ pip install fabric cuisine
$ pip install paramiko==1.10
```

## Install

```
$ vagrant up
$ fab main
```

## memo
- fabtoolってのを使えばもうちょいいい感じにかけそう
  - [Welcome to fabtools’s documentation! — fabtools 0.17.0 documentation](http://fabtools.readthedocs.org/en/0.17.0/)
- cuisineを使えば冪等性が担保されるがchef程ではないみたい（がっつり検証してないのでなんともいえない）

## other
- [複数プロジェクトを抱えるチームでのデプロイ自動化 | SOTA](http://deeeet.com/writing/2014/10/30/fabric/)
- [意識の低い自動化](http://www.slideshare.net/greenasparagus/ss-42424543)
- [Fabric Python Developers Festa 2013.03 #pyfes // Speaker Deck](https://speakerdeck.com/drillbits/fabric-python-developers-festa-2013-dot-03-number-pyfes)
