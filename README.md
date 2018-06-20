cvmfs-manage-replicas
=====================

For documentation on manage-replicas see the comments in [manage-replicas.conf](https://github.com/cvmfs-contrib/cvmfs-manage-replicas/blob/master/manage-replicas.conf).

To invoke from cron, use the additional script manage-replicas-log which allows $MAXPARALLELMANAGE replicas to happen in parallel and combines their output in /var/log/cvmfs/manage-replicas.log.
