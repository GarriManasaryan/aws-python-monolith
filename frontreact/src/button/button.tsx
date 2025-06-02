import React, { useEffect, useState } from 'react'
import './style.css';
import { axiosConf, backofficeConf } from '../axiosConf';
import endpointConfigurator from '../endpointConfigurator';

interface IProduct {
    name: string;
}

function MyButton() {

    const [name, setName] = useState('');
    const [allNames, setAllName] = useState<IProduct[]>([]);

    const fetchUsers = () => {
        axiosConf.get('/users')
        .then((response) => {
            setAllName(response.data)
        })
    }

    useEffect(()=>{
        fetchUsers()
    }, [])

    const onNameChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        setName(event.target.value);
    };

    const onClickSave = () => {
        axiosConf.post("/users", {"name":name})
    };

    const onClickGetAll = () => {
        console.log(process.env.REACT_APP_BASE_URL)
        fetchUsers()
    };

    return (
        <div style={{
                display: "flex", 
                flexDirection: "column", 
                flexWrap: "wrap", 
                gap: "2rem",
                padding: "20rem"
            }}>
            <div>{endpointConfigurator('/api')}</div>
            <input id="myText" type="text" onChange={(e) => onNameChange(e)}></input>
            <button onClick={() => onClickSave()}>send save from input</button>
            <button onClick={() => onClickGetAll()}>get all</button>
            <div>
                <ul>
                    {allNames.map((i) => (
                        <li key={i.name}>{i.name}</li>
                    ))}
                </ul>
            </div>
        </div>
    )
}

export default MyButton