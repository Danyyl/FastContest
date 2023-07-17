import React, { useEffect, useRef, useState } from 'react';
import { Link, useLocation } from 'react-router-dom';
import '../styles/NavBar.css';
import {Container} from "@mui/material";

const sidebarNavItems = [
    {
        display: 'Tasks',
        to: '/',
        section: ''
    },
    {
        display: 'Profile',
        to: '/me',
        section: 'me'
    },
    {
        display: 'My Tasks',
        to: '/my-tasks',
        section: 'my-tasks'
    },
    {
        display: 'Statistic',
        to: '/stat',
        section: 'stat'
    },
]

const NavBar = () => {
    const [activeIndex, setActiveIndex] = useState(1);
    const [stepHeight, setStepHeight] = useState(0);
    const sidebarRef = useRef();
    const indicatorRef = useRef();
    const location = useLocation();

    useEffect(() => {
        setTimeout(() => {
            const sidebarItem = sidebarRef.current.querySelector('.sidebar__menu__item');
            indicatorRef.current.style.height = `${sidebarItem.clientHeight}px`;
            setStepHeight(sidebarItem.clientHeight);
        }, 50);
    }, []);

    // change active index
    useEffect(() => {
        const curPath = window.location.pathname.split('/')[1];
        const activeItem = sidebarNavItems.findIndex(item => item.section === curPath) >= 0 ? sidebarNavItems.findIndex(item => item.section === curPath) : 0;
        setActiveIndex(curPath.length === 0 ? 0 : activeItem);
    }, [location]);

    return <Container className='sidebar'>
        <div className="sidebar__logo">
            Menu
        </div>
        <div ref={sidebarRef} className="sidebar__menu">
            <div
                ref={indicatorRef}
                className="sidebar__menu__indicator"
                style={{
                    transform: `translateX(-50%) translateY(${activeIndex * stepHeight}px)`
                }}
            ></div>
            {
                sidebarNavItems.map((item, index) => (
                    <Link to={item.to} key={index}>
                        <div className={`sidebar__menu__item ${activeIndex === index ? 'active' : ''}`}>
                            <div className="sidebar__menu__item__icon">
                                {item.icon}
                            </div>
                            <div className="sidebar__menu__item__text">
                                {item.display}
                            </div>
                        </div>
                    </Link>
                ))
            }
        </div>
    </Container>;
};

export default NavBar;