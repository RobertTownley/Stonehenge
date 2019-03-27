function getServerList() {
  const servers = [
    {
      id: 25,
      name: 'Personal Server',
    },
    {
      id: 29,
      name: 'Other Server',
    },
    {
      id: 35,
      name: 'Mystery Server',
    },
  ]
  return servers
}

export default {
  getServerList,
}
